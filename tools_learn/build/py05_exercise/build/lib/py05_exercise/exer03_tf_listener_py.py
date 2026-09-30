"""  
    需求：监听两只乌龟相对于world坐标系的tf坐标变换关系。
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
from tf2_ros import TransformListener, Buffer
from geometry_msgs.msg import Twist
import math
# 3.自定义节点类；
class Exer03_TF_Listener(Node):
    def __init__(self):
        super().__init__("Exer03_TF_Listener_node_py")

        #声明参数服务
        self.declare_parameter("father_frame", "turtle2")
        self.declare_parameter("child_frame", "turtle1")

        #解析传入的参数
        self.father_frame=self.get_parameter("father_frame").get_parameter_value().string_value
        self.child_frame=self.get_parameter("child_frame").get_parameter_value().string_value

        #创建缓存
        self.buffer = Buffer()
        #创建监听器
        self.listener = TransformListener(self.buffer, self)

        #创建速度发布
        self.cmd_pub=self.create_publisher(Twist, f'/{self.father_frame}/cmd_vel', 10)

        #创建定时器发布
        self.timer = self.create_timer(0.5, self.timer_callback)

    #创建回调函数
    def timer_callback(self):
        if self.buffer.can_transform(self.father_frame, self.child_frame, rclpy.time.Time()):
            #获取两只乌龟的相对坐标变换关系
            trans = self.buffer.lookup_transform(self.father_frame, self.child_frame, rclpy.time.Time())
            #打印坐标变换关系
            self.get_logger().info(f"坐标变换关系：\n{trans}")
            #创建速度消息对象
            cmd_msg=Twist()
            #设置线速度
            cmd_msg.linear.x=0.5*math.sqrt(math.pow(trans.transform.translation.x,2)+
                                           math.pow(trans.transform.translation.y,2))
            #设置角速度
            cmd_msg.angular.z=1.0*math.atan2(trans.transform.translation.y,
                                             trans.transform.translation.x)
            

            #发布速度消息
            self.cmd_pub.publish(cmd_msg)
        else:
            self.get_logger().info("数据未获取")




def main():
    # 2.初始化ROS2客户端；
    rclpy.init()
    # 4.调用spain函数，并传入节点对象；
    rclpy.spin(Exer03_TF_Listener())
    # 5.资源释放。 
    rclpy.shutdown()

if __name__ == '__main__':
    main()