from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute


class MirrorNode(Node):
    def __init__(self):
        super().__init__('mirror_node')
        # 订阅乌龟1的速度
        self.sub_vel = self.create_subscription(
            Twist,
            '/turtlesim1/turtle1/cmd_vel',
            self.vel_callback,
            10
        )
        # 发布镜像速度给乌龟2
        self.pub_vel = self.create_publisher(
            Twist,
            '/turtlesim2/turtle1/cmd_vel',
            10
        )
        self.pose = None
        self.pose_sub = self.create_subscription(
            Pose,
            '/turtlesim2/turtle1/pose',
            self.pose_callback,
            10
        )
        self.teleport_client = self.create_client(
            TeleportAbsolute,
            '/turtlesim2/turtle1/teleport_absolute'
        )
        self.rotate_timer = self.create_timer(0.1, self.rotate_turtle)

    def pose_callback(self, msg: Pose):
        self.pose = msg

    def rotate_turtle(self):
        if self.pose is None or not self.teleport_client.service_is_ready():
            return

        request = TeleportAbsolute.Request()
        request.x = self.pose.x
        request.y = self.pose.y
        request.theta = 0.0
        #3.1415926
        self.teleport_client.call_async(request)
        self.rotate_timer.cancel()
        self.get_logger().info('乌龟2已掉头180度，镜像节点就绪')

    def vel_callback(self, msg: Twist):
        # =========镜像核心逻辑=========
        # linear.x取反：乌龟1向前，乌龟2向后；乌龟1向后，乌龟2向前
        # angular.z取反：乌龟1左转，乌龟2右转；乌龟1右转，乌龟2左转
        mirror_twist = Twist()
        mirror_twist.linear.x = msg.linear.x
        mirror_twist.angular.z = msg.angular.z
        self.pub_vel.publish(mirror_twist)


def main(args=None):
    rclpy.init(args=args)
    node = MirrorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



#
"""

source /opt/ros/jazzy/setup.bash
source ~/ros2_learn/tongxun_learn/install/setup.bash
ros2 run turtlesim turtle_teleop_key --ros-args -r /turtle1/cmd_vel:=/turtlesim1/turtle1/cmd_vel
"""
