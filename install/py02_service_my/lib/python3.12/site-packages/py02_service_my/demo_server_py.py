#创建服务端
import rclpy
from rclpy.node import Node
from student_interfaces.srv import Addints

class DemoServer(Node):
    def __init__(self):
        super().__init__("my_server_node")
        self.get_logger().info("服务端节点创建成功")

        #创建服务端
        self.srv=self.create_service(Addints,"add_ints",self.add_callback)

    #回调函数
    def add_callback(self,request,response):
        response.sum=request.num1+request.num2
        self.get_logger().info("请求数据：num1=%d,num2=%d"%(request.num1,request.num2))
        self.get_logger().info("响应数据：sum=%d"%(response.sum))
        return response


def main():
    #初始化ros
    rclpy.init()
    #创建节点对象
    node=DemoServer()
    #挂起
    rclpy.spin(node)
    #释放ros资源
    rclpy.shutdown()


if __name__ == '__main__':
    main()
