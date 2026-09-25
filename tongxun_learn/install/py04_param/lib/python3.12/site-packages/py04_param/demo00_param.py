import rclpy
from rclpy.node import Node

#创建参数节点
class DemoParam(Node):
    def __init__(self):
        super().__init__(
            "my_param_node",
            allow_undeclared_parameters=True,
        )
        self.get_logger().info("参数节点创建成功")

        # 声明参数，外部节点才能通过 ROS 2 参数服务查询和修改。
        self.declare_parameter("car_name", "my_car")
        self.declare_parameter("hight", 100)
        self.declare_parameter("weigth", 200)

        # 读取并打印参数。
        self.get_logger().info(
            f"参数P1名字:car_name 参数P1值:{self.get_parameter('car_name').value}"
        )
        self.get_logger().info(
            f"参数P2名字:hight 参数P2值:{self.get_parameter('hight').value}"
        )
        self.get_logger().info(
            f"参数P3名字:weigth 参数P3值:{self.get_parameter('weigth').value}"
        )


def main():
    #初始化ros
    rclpy.init()
    #创建客户端对象
    node=DemoParam()
    #循环等待回调函数
    rclpy.spin(node)
    #释放资源
    rclpy.shutdown()


if __name__ == '__main__':
    main()
