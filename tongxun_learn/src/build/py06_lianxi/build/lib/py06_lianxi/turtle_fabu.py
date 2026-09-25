import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleControlPub(Node):
    def __init__(self):
        super().__init__('turtle_control_pub')
        # 发布速度指令话题
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.2, self.timer_callback)
        self.safe_flag = True

    def timer_callback(self):
        msg = Twist()
        if self.safe_flag:
            msg.linear.x = 0.3  # 前进速度
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0 # 越界，停止
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()