

"""  
    需求：编写服务端，接收客户端发送请求，提取其中两个整型数据，相加后将结果响应回客户端。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建服务端；
            3-2.处理请求数据并响应结果。
        4.调用spin函数，并传入节点对象；
        5.释放资源。

"""
import rclpy
from rclpy.node import Node
from student_interfaces.srv import Addints

#创建服务段节点
class Demo01Server(Node):
    def __init__(self):
        super().__init__("my_server_node")
        self.get_logger().info("服务端节点创建成功！")

        #创建服务端  参数：接口类型 话题名称 回调
        server=self.create_service(Addints,"add_ints",self.on_add)

    #参数1 请求对象   参数2返回值
    def on_add(self,request,response):
        response.sum=request.num1+request.num2
        self.get_logger().info(f"接收到请求数据：{request.num1}+{request.num2}={response.sum}")
        return response



def main():
    rclpy.init()

    #调用spin函数，并传入节点对象
    node = Demo01Server()
    rclpy.spin(node)

    #消除
    rclpy.shutdown()


   


if __name__ == '__main__':
    main()
