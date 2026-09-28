"""  
    需求：编写静态坐标变换程序，执行时传入两个坐标系的相对位姿关系以及父子级坐标系id，
         程序运行发布静态坐标变换。 传入x y z roll pitch yaw frame_id child_frame_id
    步骤：
        1.导包；
        2.判断终端传入的参数是否合法；
        3.初始化 ROS 客户端；
        4.定义节点类；
            4-1.创建静态坐标变换发布方；
            4-2.组织并发布消息。
        5.调用 spin 函数，并传入对象；
        6.释放资源。 

"""

import sys
from geometry_msgs.msg import TransformStamped
import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
import tf_transformations
from rclpy.logging import get_logger

#创建节点类
class TFStaticFramePublisher(Node):
    def __init__(self,args):
        super().__init__('tf_static_frame_publisher')
        #创建广播对象
        self.broadcaster = StaticTransformBroadcaster(self)
        #组织消息
        self.TF_denf(args)
    def TF_denf(self,args):
        #创建消息对象
        ts=TransformStamped()

        #传入x y z roll pitch yaw frame_id child_frame_id
        #设置时间撮
        ts.header.stamp=self.get_clock().now().to_msg()
        #设置父级坐标系id
        ts.header.frame_id=args[7]
        #设置子级坐标系id
        ts.child_frame_id=args[8]
        #设置位置
        ts.transform.translation.x=float(args[1])
        ts.transform.translation.y=float(args[2])
        ts.transform.translation.z=float(args[3])

        #设置姿态 (欧拉角形式--->四元数形式)            roll              pitch             yaw
        q=tf_transformations.quaternion_from_euler(float(args[4]),float(args[5]),float(args[6]))
        ts.transform.rotation.x=q[0]
        ts.transform.rotation.y=q[1]
        ts.transform.rotation.z=q[2] 
        ts.transform.rotation.w=q[3]

        #发布消息
        self.broadcaster.sendTransform(ts)


def main():
     #判断传入参数
    if len(sys.argv) != 9:
        get_logger("rclpy").error("参数传入不合法")
        return        
    
    rclpy.init()
    #创建ros节点
    TFnode = TFStaticFramePublisher(sys.argv)#传入参数
    #传入spin
    rclpy.spin(TFnode)#
    #释放资源
    rclpy.shutdown()


if __name__ == '__main__':
     main()

   
