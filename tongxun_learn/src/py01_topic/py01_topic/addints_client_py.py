import sys

import rclpy
from rclpy.node import Node

from student_interfaces.srv import Addints


class AddintsClient(Node):
    def __init__(self):
        super().__init__('addints_client')
        self.client = self.create_client(Addints, 'addints')

    def call(self, num1, num2):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待 addints 服务启动...')

        request = Addints.Request()
        request.num1 = num1
        request.num2 = num2
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node = AddintsClient()

    numbers = sys.argv[1:]
    if len(numbers) == 0:
        num1, num2 = 3, 5
    elif len(numbers) == 2:
        num1, num2 = (int(value) for value in numbers)
    else:
        node.get_logger().error('用法：ros2 run py01_topic addints_client_py [num1 num2]')
        node.destroy_node()
        rclpy.shutdown()
        return

    response = node.call(num1, num2)
    if response is not None:
        node.get_logger().info(f'计算结果：{num1} + {num2} = {response.sum}')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
