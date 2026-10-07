import math

import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster


class RvizMotionDemo(Node):
    def __init__(self):
        super().__init__('rviz_motion_demo')
        self.joint_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.02, self.update)
        self.last_time = self.get_clock().now()
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.wheel_angle = 0.0
        self.wheel_radius = 0.025
        self.linear_speed = 0.05
        self.angular_speed = 0.25

    def update(self):
        now = self.get_clock().now()
        dt = (now - self.last_time).nanoseconds * 1e-9
        self.last_time = now
        dt = min(dt, 0.1)

        self.x += self.linear_speed * math.cos(self.yaw) * dt
        self.y += self.linear_speed * math.sin(self.yaw) * dt
        self.yaw += self.angular_speed * dt
        self.wheel_angle += self.linear_speed / self.wheel_radius * dt

        stamp = now.to_msg()
        transform = TransformStamped()
        transform.header.stamp = stamp
        transform.header.frame_id = 'odom'
        transform.child_frame_id = 'base_footprint_link'
        transform.transform.translation.x = self.x
        transform.transform.translation.y = self.y
        transform.transform.translation.z = 0.0
        transform.transform.rotation.z = math.sin(self.yaw / 2.0)
        transform.transform.rotation.w = math.cos(self.yaw / 2.0)
        self.tf_broadcaster.sendTransform(transform)

        joint_state = JointState()
        joint_state.header.stamp = stamp
        joint_state.name = [
            'left_front_wheel_link2base_link',
            'right_front_wheel_link2base_link',
            'left_hou_wheel_link2base_link',
            'right_hou_wheel_link2base_link',
        ]
        joint_state.position = [
            self.wheel_angle,
            self.wheel_angle,
            self.wheel_angle,
            self.wheel_angle,
        ]
        self.joint_pub.publish(joint_state)


def main(args=None):
    rclpy.init(args=args)
    node = RvizMotionDemo()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
