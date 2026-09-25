from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # 节点1：turtlesim1
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            namespace='turtlesim1',
            name='sim1'
        ),
        # 节点2：turtlesim2
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            namespace='turtlesim2',
            name='sim2'
        ),
        # 镜像处理节点（包名改成py07_jx，executable是setup注册的名字）
        Node(
            package='py07_jx',
            executable='turtle_jingxiang',
            name='mirror_node'
        )
    ])
