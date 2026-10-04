"""  
    需求：广播两只乌龟相对于word坐标系的tf坐标变换关系。
    流程：
        1.导包；
        2.初始化ROS2客户端；
        3.自定义节点类；
                        
        4.调用spain函数，并传入节点对象；
        5.资源释放。 
"""
# 1.导包；
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from turtlesim.msg import Pose
from tf_transformations import euler_from_quaternion, quaternion_from_euler


# 3.自定义节点类；
class TF_broadcasterNode(Node):
    def __init__(self):
        super().__init__("TF_broadcasterNode")
        

        self.declare_parameter("turtle", "turtle1")
        self.turtle=self.get_parameter("turtle").get_parameter_value().string_value

        #创建动态广播发布方
        self.broadcaster =TransformBroadcaster(self)

        #创建一个乌龟位置订阅节点
        self.subscription = self.create_subscription(
            Pose,
            f'/{self.turtle}/pose',
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
        t.child_frame_id = self.turtle  

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
    # 2.初始化ROS2客户端；
    rclpy.init()
    # 4.调用spain函数，并传入节点对象；
    rclpy.spin(TF_broadcasterNode())
    # 5.资源释放。 
    rclpy.shutdown()

if __name__ == '__main__':
    main()