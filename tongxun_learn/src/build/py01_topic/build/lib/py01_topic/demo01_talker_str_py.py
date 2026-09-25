"""  
    需求：以某个固定频率发送文本“hello world!”，文本后缀编号，每发送一条消息，编号递增1。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建发布方；
            3-2.创建定时器；
            3-3.组织消息并发布。
        4.调用spin函数，并传入节点对象；
        5.释放资源。
"""
import rclpy
from rclpy.node import Node
from  std_msgs.msg import String

#自定义节点类
class Talker(Node):
    def __init__(self):
        super().__init__('talker_node_py')  #节点名称
        self.get_logger().info('talker_node_py节点发布方创建！')
        #创建发布方 参数：发送数据类型  话题名称 队列长度  返回值：发布方对象
        self.pub = self.create_publisher(String, 'chatter', 10)
        #创建定时器 参数 间隔事件 回调函数
        self.timer = self.create_timer(0.5, self.timer_callback)  #0.5s回调一次
        #编号
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'hello world(python)! {self.count}'
        self.pub.publish(msg)
        self.get_logger().info(f'发布消息：{msg.data}')
        self.count += 1





def main():
    #1.初始化ros
    rclpy.init()


    #4调用spin函数，并传入节点对象
    """
    创建一个 Talker 节点对象。
    将该节点交给 ROS 2 执行器。
    持续处理节点中的回调函数，例如定时器回调、订阅回调等。
    该函数会阻塞，直到节点被关闭，通常通过 Ctrl+C 退出。
    """
    rclpy.spin(Talker())
    #5.释放
    rclpy.shutdown()


if __name__ == '__main__':
    main()
