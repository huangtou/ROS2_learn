from launch import LaunchDescription
from launch_ros.actions import Node
# 封装终端指令相关类--------------
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
# 参数声明与获取-----------------
# from launch.actions import DeclareLaunchArgument
# from launch.substitutions import LaunchConfiguration
# 文件包含相关-------------------
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# 分组相关----------------------
# from launch_ros.actions import PushRosNamespace
# from launch.actions import GroupAction
# 事件相关----------------------
# from launch.event_handlers import OnProcessStart, OnProcessExit
# from launch.actions import ExecuteProcess, RegisterEventHandler,LogInfo
# 获取功能包下share目录路径-------
from ament_index_python.packages import get_package_share_directory
import os
"""
        executable: SomeSubstitutionsType,可执行程序 节点
        package: Optional[SomeSubstitutionsType] = None,#功能包名称
        name: Optional[SomeSubstitutionsType] = None, #设置节点名称 启动后将节点设置为该名
        namespace: Optional[SomeSubstitutionsType] = None,#设置节点所在的命名空间
        exec_name: Optional[SomeSubstitutionsType] = None,#设计程序标签exec_name 用于设置启动进程显示出来的可执行程序名称或进程标签，
                                                           主要影响 launch 日志和进程标识。大多数情况下不需要设置 exec_name，使用默认值即可。
        
        parameters: Optional[SomeParameters] = None,#设置参数
        remappings: Optional[SomeRemapRules] = None,#设置话题重映射
        ros_arguments: Optional[Iterable[SomeSubstitutionsType]] = None,#为节点传参数
        arguments: Optional[Iterable[SomeSubstitutionsType]] = None,#为节点传参数
        **kwargs
"""
"""
        命名空间也会影响话题、服务和参数名称。
        /turtle1/cmd_vel
        /turtle1/pose
        例如，turtlesim 默认可能有：
        /robot1/turtle1/cmd_vel
        /robot1/turtle1/pose

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle_sim',
            namespace='robot1',
        )

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle_sim',
            namespace='robot2',
        )

        最终得到两个不同的节点：
        /robot1/turtle_sim
        /robot2/turtle_sim


"""


#演示node节点使用
def generate_launch_description():
    turtle1=Node(
        package='turtlesim',#功能包名
        executable='turtlesim_node',#节点名

        name='my_turtle1',#设置节点名称
        namespace='myturtle_',#设置节点所在的命名空间   节点的完整名称会变成：/my_turtle_/my_turtle
        #命名空间也会影响话题、服务和参数名称。

        exec_name='my_turtle1',#设计程序标签exec_name 用于设置启动进程显示出来的可执行程序名称或进程标签，
        #日志中的进程标签可能显示为：[my_turtle1-1]
        
        #用于设置节点的 ROS 2 参数。
        #方式1 直接在launch文件中设置
        # parameters=[
        # {'background_r': 255},
        # {'background_g': 0},
        # {'background_b': 0},
        # ],
        #方式2 采用yaml文件设置 这里写的是绝对路径 换个设备就会出问题 那么可以动态获取
        #
        parameters=[os.path.join(get_package_share_directory('py01_launch'),'config','turtle1.yaml')],


        # 用于设置话题重映射。('旧名称', '新名称')
        remappings=[('/cmd_vel', '/my_turtle1/cmd_vel')]
    )

    turtle2=Node(
        package='turtlesim',#功能包名
        executable='turtlesim_node',#节点名
        respawn=True,#自动重启 叉掉之后会自动启动
        name='my_turtle2',#设置节点名称
        namespace='myturtle_',
        # 用于设置话题重映射。('旧名称', '新名称')
        remappings=[('/cmd_vel', '/my_turtle2/cmd_vel')],
        exec_name='my_turtle2',#设计程序标签exec_name 用于设置启动进程显示出来的可执行程序名称或进程标签，
        #日志中的进程标签可能显示为：[my_turtle2-1]

        #用于设置节点的 ROS 2 参数。
        parameters=[
        {'background_r': 0},
        {'background_g': 255},
        {'background_b': 0},
        ]
    )
    return LaunchDescription([turtle1,turtle2])