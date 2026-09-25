"""  
    需求：订阅发布方发布的消息，并输出到终端。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建订阅方；
            3-2.处理订阅到的消息。
        4.调用spin函数,并传入节点对象,
        5.释放资源。
"""

#导包
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#创建节点
class Listener(Node):
    def __init__(self):
        super().__init__('listener_node_py')  #节点名称
        self.get_logger().info('listener_node_py节点订阅方创建！')
        #创建订阅方 参数：消息类型 话题名称 队列长度 回调函数 返回值：订阅方对象
        self.sub = self.create_subscription(String, 'chatter', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'接收到消息：{msg.data}')


def main():
    #初始化ros
    rclpy.init()

    #创建节点
    listener_node = Listener()

    #传入spin函数
    rclpy.spin(listener_node)


    #释放资源
    rclpy.shutdown()


    pass

if __name__ == '__main__':
    main()