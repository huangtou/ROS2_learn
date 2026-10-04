"""  
    需求：发布雷达坐标系中某个坐标点相对于雷达（laser）坐标系的位姿。
    步骤：
        1.导包；
        2.初始化 ROS 客户端；
        3.定义节点类；
            3-1.创建坐标点发布方；
            3-2.创建定时器；
            3-3.组织并发布坐标点消息。
        4.调用 spin 函数，并传入对象；
        5.释放资源。
"""
# 1.导包；
from geometry_msgs.msg import PointStamped
import rclpy
from rclpy.node import Node


class PubPoint(Node):
    def __init__(self):
        super().__init__('pub_point')
        # 3-1.创建坐标点发布方；
        self.pub = self.create_publisher(PointStamped, 'point', 10)
        # 3-2.创建定时器；
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.x=0.1

    # 3-3.组织并发布坐标点消息。
    def timer_callback(self):
        point_msg = PointStamped()
        point_msg.header.stamp = self.get_clock().now().to_msg()
        point_msg.header.frame_id = 'laser'
        self.x+=0.2
        point_msg.point.x = self.x
        point_msg.point.y = 0.0
        point_msg.point.z = 0.2
        self.pub.publish(point_msg)

def main():
    rclpy.init()  # 2.初始化 ROS 客户端；

    # 3.定义节点类；
    pub_point_node = PubPoint()

    rclpy.spin(pub_point_node)  # 4.调用 spin 函数，并传入对象；

    rclpy.shutdown()  # 5.释放资源。

if __name__ == '__main__':
    main()