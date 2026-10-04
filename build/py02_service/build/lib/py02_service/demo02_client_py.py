"""  
    需求：编写客户端，发送两个整型变量作为请求数据，并处理响应结果。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建客户端；
            3-2.等待服务连接；
            3-3.组织请求数据并发送；
        4.创建对象调用其功能，处理响应结果；
        5.释放资源。

"""
# 1.导包；
import sys
import rclpy
from rclpy.node import Node
from student_interfaces.srv import Addints

#自定义节点类
class Demo02Client(Node):
    def __init__(self):
        super().__init__("my_client_node")
        self.get_logger().info("客户端节点创建成功")

        #创建客户端
        self.client=self.create_client(Addints,"add_ints")

        #连接服务器
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("等待服务端连接...") 

    #发送请求
    def send_request(self):
        request=Addints.Request()
        request.num1=int(sys.argv[1])
        request.num2=int(sys.argv[2])

        #发送请求
        self.future=self.client.call_async(request)
       



#main函数

def main():

    #判断参数是不是正确
    """
    argv是终端输入的 第一个默认为程序名字 这里要输入两个
    [
    "demo02_client_py",  # sys.argv[0]：程序名
    "10",                # sys.argv[1]：第一个参数
    "20",                # sys.argv[2]：第二个参数
    ]   

    """


    if len(sys.argv) != 3:
        print("参数错误！请传入两个整型数据")
        return

    #初始化
    rclpy.init()

    #创建节点对象
    node = Demo02Client()

    #发送
    node.send_request()
    

    #处理响应
    rclpy.spin_until_future_complete(node,node.future)
    try:
        response=node.future.result()
    except Exception as e: 
        node.get_logger().error(f"服务调用失败：{e}")
    else:
        node.get_logger().info(f"响应结果：{sys.argv[1]}+{sys.argv[2]}={response.sum}")

    #释放资源
    rclpy.shutdown()


if __name__ == '__main__':
    main()