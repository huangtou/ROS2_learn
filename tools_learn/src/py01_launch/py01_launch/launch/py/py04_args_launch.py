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
    bg_r=DeclareLaunchArgument('bg_r',default_value='255',)
    bg_g=DeclareLaunchArgument('bg_g',default_value='255',)
    bg_b=DeclareLaunchArgument('bg_b',default_value='255',)

    #创建节点
    turtle1=Node(
        package='turtlesim',
        executable='turtlesim_node',
        parameters=[{
            'background_r':LaunchConfiguration('bg_r'),
            'background_g':LaunchConfiguration('bg_g'),
            'background_b':LaunchConfiguration('bg_b'),
        }]
    )


    return LaunchDescription([bg_r,bg_g,bg_b,turtle1])
 
#ros2 launch py01_launch py04_args_launch.py bg_r:=0 bg_g:=200 bg_b:=100 可以在调用的时候传参改变背景颜色
