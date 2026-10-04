"""  
  需求：编写动态坐标变换程序，启动 turtlesim_node 以及 turtle_teleop_key 后，该程序可以发布
       乌龟坐标系到窗口坐标系的坐标变换，并且键盘控制乌龟运动时，乌龟坐标系与窗口坐标系的相对关系
       也会实时更新。

  步骤：
    1.导包；
    2.初始化 ROS 客户端；
    3.定义节点类；
      3-1.创建动态坐标变换发布方；
      3-2.创建乌龟位姿订阅方；
      3-3.根据订阅到的乌龟位姿生成坐标帧并广播。
    4.调用 spin 函数，并传入对象；
    5.释放资源。
"""

import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from turtlesim.msg import Pose
from tf_transformations import euler_from_quaternion, quaternion_from_euler




class DongtaiBroadcaster(Node):
    def __init__(self):
        super().__init__('dongtai_broadcaster')
        self.get_logger().info('DongtaiBroadcaster node has been started.')
        #创建动态广播发布方
        self.broadcaster =TransformBroadcaster(self)

        #创建一个乌龟位置订阅节点
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        #创建回调函数
    def pose_callback(self,pose):
        #创建消息对象
        t = TransformStamped()

        #设置时间戳
        t.header.stamp = self.get_clock().now().to_msg()
        #设置父级坐标系id
        t.header.frame_id = 'world'
        #设置子级坐标系id
        t.child_frame_id = 'turtle1'

        #设置位置
        t.transform.translation.x = pose.x
        t.transform.translation.y = pose.y
        t.transform.translation.z = 0.0

        #设置姿态 (欧拉角形式--->四元数形式)
        q= quaternion_from_euler(0, 0, pose.theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        #发布消息
        self.broadcaster.sendTransform(t)        

def main():
    rclpy.init()

    dt_broadcaster = DongtaiBroadcaster()
    rclpy.spin(dt_broadcaster)

    rclpy.shutdown()
    pass

if __name__ == '__main__':
    main()