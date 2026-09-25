import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleMonitorSub(Node):
    def __init__(self):
        super().__init__('turtle_monitor_sub')
        # 订阅乌龟位姿话题
        self.sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)
        self.control_pub_node = None

    def pose_callback(self, msg):
        x = msg.x
        y = msg.y
        # turtlesim窗口x范围大约0~11
        if x > 8.0 or x<2:
            self.get_logger().warn(f"乌龟x={x:.2f}，快要撞墙！停止运动")
            # 调用发布节点的标志位，停止乌龟
            if self.control_pub_node is not None:
                self.control_pub_node.safe_flag = False
        else:
            self.get_logger().info(f"乌龟正常，x={x:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMonitorSub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()