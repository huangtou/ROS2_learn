#创建参数服务的服务端

#导包
import rclpy
from rclpy.node import Node

class DemoParamServer(Node):
    def __init__(self):
        #如果允许修改，需要声明
        super().__init__("my_param_server", allow_undeclared_parameters=True)
        self.get_logger().info("参数服务端创建成功")

    #增
    def add_param(self):
        self.get_logger().info("添加变量")

        self.declare_parameter("name", "hello")  #声明参数
        self.declare_parameter("age", 18)  #声明参数
        self.declare_parameter("height", 1.75)  #声明参数

        #在终端 用ros2 param list /my_param_server 可以查看参数列表
        #ros2 param get /my_param_server age  my_param_server 是节点名称

    #删
    def del_param(self):
        self.get_logger().info("删除变量")

        self.get_logger().info(f"删除前是否有age参数{self.has_parameter('age')}")
        self.undeclare_parameter("age")
        self.get_logger().info(f"删除后是否有age参数{self.has_parameter('age')}")


    #改
    def set_param(self):
        self.get_logger().info("修改变量")

        self.set_parameters([rclpy.Parameter('age',value=9090)])

        self.get_logger().info(f"修改后age为{self.get_parameter('age').value}")

    #查
    def get_param(self):
        self.get_logger().info("获取变量")
        #获取指定参数
        name_param=self.get_parameter("name")
        #处理打印
        self.get_logger().info(f"参数名{name_param.name},参数值{name_param.value}")

        #获取多个参数
        params=self.get_parameters(["name","age","height"])
        for param in params:
            self.get_logger().info(f"参数名{param.name},参数值{param.value}")

        #判断参数是否存在
        self.get_logger().info(f"参数age是否存在{self.has_parameter("age")}")
        self.get_logger().info(f"参数sex是否存在{self.has_parameter("sex")}")
        




def main():
    #初始化ros
    rclpy.init()

    #创建客户端对象
    param_server_node=DemoParamServer()

    param_server_node.add_param()
    
    param_server_node.set_param()
    param_server_node.get_param()

    param_server_node.del_param()

    
    rclpy.spin(param_server_node)

    #释放资源
    rclpy.shutdown()