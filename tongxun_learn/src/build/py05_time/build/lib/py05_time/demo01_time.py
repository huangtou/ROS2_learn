#rate使用
import rclpy
from rclpy.node import Node
import time
import threading
from rclpy.time import Time
from rclpy.duration import Duration

"""
Time      = 什么时候
Duration  = 多长时间
Rate      = 多久循环一次
"""

#定义节点
class RateNode(Node):
    def __init__(self):
        super().__init__('rate_node')
        #创建定时器，周期为1s
        #self.demo_rate()
        #self.demo_time()

        self.demo_duration()

    def demo_time(self):
        #设置当时间
        t1=Time(seconds=5, nanoseconds=500000000)#第一个设置秒 第二个设置纳秒

        #获取当前时间
        now_time=self.get_clock().now()

        self.get_logger().info(f"t1: 秒：{t1.seconds_nanoseconds()[0]} 纳秒：{t1.seconds_nanoseconds()[1]}")
        self.get_logger().info(f"now_time: 秒：{now_time.seconds_nanoseconds()[0]} 纳秒：{now_time.seconds_nanoseconds()[1]}")

    def demo_rate(self):
        #创建Rate对象
        self.rate=self.create_rate(1)  # 1Hz 延时一秒
        # while rclpy.ok():
        #     self.get_logger().info('hello world')
        #     #self.rate.sleep()  # 延时一秒 #这样写只会打印一次就挂起 解决是创建子线程
        #解决1 用time.sleep()
        #     time.sleep(1)  # 延时一秒 这样可以但是这样和rate对象就没有关系了

        #解决2 创建子线程
        thread=threading.Thread(target=self.do_some)
        thread.start()
        

    def do_some(self):
        while rclpy.ok():
            self.get_logger().info('hello world')
            self.rate.sleep()  # 延时一秒

    def demo_duration(self):
        #创建Duration对象
        duration=Duration(seconds=2, nanoseconds=500000000)
        self.get_logger().info(f"duration: {duration.nanoseconds}")


def main():
    #初始化ros
    rclpy.init()
    #创建节点
    node=RateNode()
    #循环等待回调函数
    rclpy.spin(node)


    #释放ros
    rclpy.shutdown()