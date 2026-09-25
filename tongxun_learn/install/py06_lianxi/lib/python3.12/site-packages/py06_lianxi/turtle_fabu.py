import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleControlPub(Node):
    def __init__(self):
        super().__init__('turtle_control_pub')
        # 发布速度指令话题
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.2, self.timer_callback)
        self.safe_flag = True

        # turtlesim 的有效区域大约是 0.0 ~ 11.0
        # 提前留出 1.0 的安全距离
        self.min_x = 1.0
        self.max_x = 10.0
        self.min_y = 1.0
        self.max_y = 10.0

        # 订阅乌龟位置
        self.pose_sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

    def timer_callback(self):
        msg = Twist()
        if self.safe_flag:
            msg.linear.x = 0.3  # 前进速度
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0 # 越界，停止
            msg.angular.z = 0.0
            # 停止定时器，避免继续发布
            self.timer.cancel()
        self.pub.publish(msg)

    def pose_callback(self, msg):
        if not self.safe_flag:
            return
        # 判断乌龟是否接近边界
        out_of_safe_area = (msg.x < self.min_x or msg.x > self.max_x
            or msg.y < self.min_y or msg.y > self.max_y)

        if out_of_safe_area:
            self.safe_flag = False

            # 立即发布停止指令
            stop_msg = Twist()
            stop_msg.linear.x = 0.0
            stop_msg.angular.z = 0.0
            self.pub.publish(stop_msg)

            self.get_logger().info(
                f'检测到边界，停止运动。'
                f'当前位置：x={msg.x:.2f}, y={msg.y:.2f}'
            )
            
            # 取消速度定时器
            self.timer.cancel()
        






def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()