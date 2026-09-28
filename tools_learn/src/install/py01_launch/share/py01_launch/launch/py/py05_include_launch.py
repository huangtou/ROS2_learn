from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import os
# 封装终端指令相关类--------------
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
# 参数声明与获取-----------------
# from launch.actions import DeclareLaunchArgument
# from launch.substitutions import LaunchConfiguration
# 文件包含相关-------------------
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
# 分组相关----------------------
# from launch_ros.actions import PushRosNamespace
# from launch.actions import GroupAction
# 事件相关----------------------
# from launch.event_handlers import OnProcessStart, OnProcessExit
# from launch.actions import ExecuteProcess, RegisterEventHandler,LogInfo
# 获取功能包下share目录路径-------
# from ament_index_python.packages import get_package_share_directory

#在当前launch文件中包含其他launch文件
def generate_launch_description():
    include_launch=IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(  #封装其他launch文件
            os.path.join(
                get_package_share_directory('py01_launch'),
                'launch/py',
                'py04_args_launch.py',
            )
        ),
        launch_arguments=[('bg_r', '0'), ('bg_g', '10'), ('bg_b', '20')]#传参
    )
    return LaunchDescription([include_launch])


#install/py01_launch/share/py01_launch/launch/py/py05_include_launch.py