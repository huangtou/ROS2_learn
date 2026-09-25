import rclpy
from rclpy.node import Node

from student_interfaces.srv import Addints


class AddintsServer(Node):
    def __init__(self):
        super().__init__('addints_server')
        self.service = self.create_service(
            Addints,
            'addints',
            self.addints_callback,
        )
        self.get_logger().info('Addints 服务已启动，服务名：addints')

    def addints_callback(self, request, response):
        response.sum = request.num1 + request.num2
        self.get_logger().info(
            f'收到请求：{request.num1} + {request.num2} = {response.sum}'
        )
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddintsServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
