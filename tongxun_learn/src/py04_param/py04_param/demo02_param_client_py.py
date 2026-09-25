import rclpy
from rcl_interfaces.msg import ParameterType
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.parameter_client import AsyncParameterClient


class DemoParamClient(Node):
    """操作 /my_param_node 提供的 ROS 2 参数服务。"""

    def __init__(self):
        super().__init__("my_param_client")
        self.client = AsyncParameterClient(self, "/my_param_node")

    def _call(self, future):
        """等待参数服务响应，并在服务不可用时抛出明确错误。"""
        rclpy.spin_until_future_complete(self, future)
        if future.exception() is not None:
            raise RuntimeError(f"参数服务调用失败: {future.exception()}")
        return future.result()

    def list_params(self):
        """查：列出目标节点当前已经声明的参数。"""
        response = self._call(self.client.list_parameters())
        names = response.result.names
        self.get_logger().info(f"/my_param_node 的参数: {names}")
        return names

    def get_params(self, names):
        """查：读取指定参数的值。"""
        response = self._call(self.client.get_parameters(names))
        for name, parameter in zip(names, response.values):
            if parameter.type == ParameterType.PARAMETER_NOT_SET:
                self.get_logger().warning(f"参数不存在或未设置: {name}")
            else:
                value = self._parameter_value(parameter)
                self.get_logger().info(
                    f"读取参数: {name} = {value}"
                )
        return response.values

    @staticmethod
    def _parameter_value(parameter):
        """将 ROS 2 ParameterValue 消息转换为实际参数值。"""
        value_fields = {
            ParameterType.PARAMETER_BOOL: "bool_value",
            ParameterType.PARAMETER_INTEGER: "integer_value",
            ParameterType.PARAMETER_DOUBLE: "double_value",
            ParameterType.PARAMETER_STRING: "string_value",
            ParameterType.PARAMETER_BYTE_ARRAY: "byte_array_value",
            ParameterType.PARAMETER_BOOL_ARRAY: "bool_array_value",
            ParameterType.PARAMETER_INTEGER_ARRAY: "integer_array_value",
            ParameterType.PARAMETER_DOUBLE_ARRAY: "double_array_value",
            ParameterType.PARAMETER_STRING_ARRAY: "string_array_value",
        }
        field_name = value_fields.get(parameter.type)
        if field_name is None:
            return None
        return getattr(parameter, field_name)

    def describe_params(self, names):
        """查：读取指定参数的类型和描述信息。"""
        response = self._call(self.client.describe_parameters(names))
        for descriptor in response.descriptors:
            self.get_logger().info(
                f"参数描述: {descriptor.name}, "
                f"类型={descriptor.type}, "
                f"描述={descriptor.description or '无'}"
            )
        return response.descriptors

    def set_params(self, parameters):
        """改：修改目标节点已经声明的参数。"""
        response = self._call(self.client.set_parameters(parameters))
        for parameter, result in zip(parameters, response.results):
            if result.successful:
                self.get_logger().info(
                    f"修改成功: {parameter.name} = {parameter.value}"
                )
            else:
                self.get_logger().error(
                    f"修改失败: {parameter.name}: {result.reason}"
                )
        return response.results

    def add_param(self, parameter):
        """增：尝试新增参数；普通远程参数服务不能保证声明新参数。"""
        self.get_logger().info(f"尝试新增参数: {parameter.name}")
        result = self.set_params([parameter])[0]
        if not result.successful:
            self.get_logger().warning(
                "新增失败：/my_param_node 未允许未声明参数。"
                "参数必须由目标节点自己 declare_parameter()。"
            )
        return result

    def delete_param(self, name):
        """删：远程参数服务没有 undeclare_parameter 接口。"""
        self.get_logger().error(
            f"删除失败: ROS 2 不提供远程删除参数服务 ({name})。"
            "必须在 /my_param_node 节点内部调用 undeclare_parameter()。"
        )
        return False


def main():
    rclpy.init()
    node = DemoParamClient()

    try:
        if not node.client.wait_for_services(timeout_sec=5.0):
            raise RuntimeError(
                "等待 /my_param_node 参数服务超时。"
                "请先运行: ros2 run py04_param demo00_param"
            )

        # 查：列出、读取和描述目标节点的参数。
        names = node.list_params()
        if names:
            node.get_params(names)
            node.describe_params(names)

        # # 改：对当前 demo00 中的参数发起修改请求。
        node.set_params([
            Parameter("car_name", value="new_car"),
            Parameter("hight", value=180),
            Parameter("weigth", value=250),
        ])

        # 增、删：明确展示 ROS 2 对远程操作的限制。
        node.add_param(Parameter("color", value="red"))

        names = node.list_params()
        if names:
            node.get_params(names)
            node.describe_params(names)

        #node.delete_param("car_name")
    except (RuntimeError, ValueError) as error:
        node.get_logger().error(str(error))
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()