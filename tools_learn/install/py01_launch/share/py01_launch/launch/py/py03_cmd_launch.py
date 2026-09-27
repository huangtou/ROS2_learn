from launch import LaunchDescription
from launch_ros.actions import Node
# 封装终端指令相关类--------------
from launch.actions import ExecuteProcess
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
# from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    turtle1=Node(
        package='turtlesim',
        executable='turtlesim_node',
    )

    #封装终端命令 打印乌龟位姿
    cmd=ExecuteProcess(
        cmd=["ros2 topic echo /turtle1/pose"],
        #可以分成多个字符串 
        #cmd=["ros2 topic", "echo", "/turtle1/pose"],
        shell=True,#表示按照终端命令执行
        output='both',#表示在终端和日志都显示输出
    )
    return LaunchDescription([turtle1,cmd])#要包含才会有用