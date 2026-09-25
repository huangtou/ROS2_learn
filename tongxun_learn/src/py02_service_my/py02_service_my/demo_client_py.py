#创建客服端

import rclpy
from rclpy.node import Node
from student_interfaces.srv import Addints
import sys


#创建客户端节点
class DemoClient(Node):
    def __init__(self):
        super().__init__("my_client_node")
        self.get_logger().info("客户端节点创建成功")

        #创建客户端
        self.cli=self.create_client(Addints,"add_ints")

        #连接服务端
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("等待服务端连接...")

        #发送请求
        self.req=Addints.Request()
        self.req.num1=int(sys.argv[1])
        self.req.num2=int(sys.argv[2])

        #异步发送请求
        self.future=self.cli.call_async(self.req)

        rclpy.spin_until_future_complete(self,self.future)
        try:
            response=self.future.result()
        except Exception as e:
            self.get_logger().error(f"服务调用失败：{e}")
        else:
            self.get_logger().info(f"响应结果：{sys.argv[1]}+{sys.argv[2]}={response.sum}")
        


def main():

    if len(sys.argv) != 3:
        print("参数错误！请传入两个整型数据")
        return
    #初始化ros
    rclpy.init()
    #创建节点对象
    node=DemoClient()
    #挂起
    #rclpy.spin(node)
    #释放ros资源
    rclpy.shutdown()


if __name__ == '__main__':
    main()
