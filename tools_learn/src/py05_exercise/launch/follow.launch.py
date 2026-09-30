from launch import LaunchDescription
from launch_ros.actions import Node
# 封装终端指令相关类--------------
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
# 参数声明与获取-----------------
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
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
# from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    #声明变量
    turtle1 = DeclareLaunchArgument(name="turtle1",default_value="turtle1")
    turtle2 = DeclareLaunchArgument(name="turtle2",default_value="turtle2")
    t1=Node(
        package="turtlesim",
        executable="turtlesim_node",
    )

    t2=Node(
        package="py05_exercise",
        executable="exer01_spawn_py",
        parameters=[{
                    'name':LaunchConfiguration('turtle2'),
                }]

    )

    #广播两只乌龟坐标变换
    tf1=Node(
        package="py05_exercise",
        executable="exer02_tf_broadcaster_py",
        name="tf1",
    )

    tf2=Node(
        package="py05_exercise",
        executable="exer02_tf_broadcaster_py",
        parameters=[{
                    'turtle':LaunchConfiguration('turtle2'),
                }]
    )

    #两只乌龟坐标变换
    tf_listers=Node(
        package="py05_exercise",
        executable="exer03_tf_listener_py",
        name="tf_listers",
        parameters=[{"father_frame":LaunchConfiguration("turtle2"),"child_frame":LaunchConfiguration("turtle1")}]
    )

    return LaunchDescription([turtle1, turtle2, t1, t2, tf1, tf2,tf_listers])