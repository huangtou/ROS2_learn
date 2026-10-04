"""  
  需求：编写客户端，发送请求生成一只新的乌龟。

  步骤：
    1.导包；
    2.初始化 ROS2 客户端；
    3.定义节点类；
      3-1.声明并获取参数；
      3-2.创建客户端；
      3-3.等待服务连接；
      3-4.组织请求数据并发送；
    4.创建对象调用其功能,并处理响应；
    5.释放资源。  
"""

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class SpawnTurtleClient(Node):
    def __init__(self):
        super().__init__("create_new_turtle")
        #参数服务声明乌龟消息
        self.declare_parameter("x", 3.5)
        self.declare_parameter("y", 3.5)   
        self.declare_parameter("theta", 1.57)
        self.declare_parameter("name", "turtle2")

        #获取参数
        self.x = self.get_parameter("x").get_parameter_value().double_value
        self.y = self.get_parameter("y").get_parameter_value().double_value
        self.theta = self.get_parameter("theta").get_parameter_value().double_value
        self.name = self.get_parameter("name").get_parameter_value().string_value

        #创建客服端
        self.client=self.create_client(Spawn, "/spawn")

        #等待服务连接
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("服务未连接,等待中...")

    #发送消息
    def send_request(self):
        #组织请求数据
        request = Spawn.Request()
        request.x = self.x
        request.y = self.y
        request.theta = self.theta
        request.name = self.name

        #发送请求
        self.future = self.client.call_async(request)



def main():
    #初始化ros2
    rclpy.init()

    node_new_turtle = SpawnTurtleClient()

    node_new_turtle.send_request()

    #处理结果 #等到有结果
    rclpy.spin_until_future_complete(node_new_turtle, node_new_turtle.future)

    result=node_new_turtle.future.result()  #获取结果
    if (result.name):
        node_new_turtle.get_logger().info(f"新乌龟已生成: {result.name}")
    else:
        node_new_turtle.get_logger().info("新乌龟生成失败.乌龟重名了")

    #释放资源
    rclpy.shutdown()


if __name__ == "__main__":
    main()