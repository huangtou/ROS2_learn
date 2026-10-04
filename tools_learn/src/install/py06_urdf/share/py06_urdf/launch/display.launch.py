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
from ament_index_python.packages import get_package_share_directory#获取shall目录

#加载urdf文件并在 rviz中显示

#导入parameters对象
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command#封装指令执行 


#基础
# p_value = ParameterValue(Command(['xacro ', get_package_share_directory("py06_urdf")+'/urdf/urdf/demo01_helloword.urdf']))

# def generate_launch_description():
    
#     # 加载urdf 比较难
#     robot_state_pub=Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         parameters=[{'robot_description': p_value}],
#     )

#     #启动rviz2
#     rviz1=Node(
#         package='rviz2',
#         executable='rviz2',
#     )
#     return LaunchDescription([rviz1,robot_state_pub])


#优化 1 添加join_state_publisher 节点 实现对非固定关节的处理
#优化 2 添加rviz2配置文件
#优化 3 动态传入urdf文件 封装为参数


#如何动态传参


#xxxx launch xxxx.py model:='ros2 pkg prefix --share py06_urdf'/urdf/urdf/demo01_helloword.urdf
#前面单引号内容等价于 get_package_share_directory("py06_urdf") 

#用这个
#model:="$(ros2 pkg prefix --share py06_urdf)/urdf/urdf/demo02_link.urdf"

model=DeclareLaunchArgument(name='model',default_value=get_package_share_directory("py06_urdf")+'/urdf/urdf/demo05_car.urdf')
p_value = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]))

def generate_launch_description():
    
    # 加载urdf 比较难
    robot_state_pub=Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': p_value}],
    )

    #优化1 
    joint_state_pub=Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
    )
    #启动rviz2 
    rviz1=Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', get_package_share_directory("py06_urdf")+'/rviz/urdf1.rviz'],
    )
    return LaunchDescription([model,rviz1,robot_state_pub,joint_state_pub])

"""
robot_state_publisher与robot_state_publisher_gui的区别：
1. robot_state_publisher_gui是robot_state_publisher的图形化版本，提供了一个GUI界面，允许用户通过图形界面来设置和调整机器人的关
节状态。它适用于那些希望通过图形界面进行交互的用户，尤其是在调试和测试阶段。
2. robot_state_publisher_gui通常会包含一个关节状态发布器的GUI界
面，用户可以通过滑块、按钮等控件来调整机器人的关节角度，从而实时观察机器人的运动效果。
3. robot_state_publisher_gui可能会提供更多的可视化选项，例如显示关节角度的数值、显示关节的运动轨迹等，以便用户更好地理解机器人的运动状态。
4. robot_state_publisher_gui可能会提供一些额外的功能，例如记录关节状态、导出关节状态数据等，以便用户进行分析和后续处理。
5. robot_state_publisher_gui可能会提供一些调试工具，例如显示关节的速度、加速度等信息，以帮助用户进行性能分析和优化。

他们两个作用一样都能够发布关节状态信息，但robot_state_publisher_gui提供了更直观和交互式的方式来进行关节状态的设置和调整，适用于那些希望通过图形界面进行交互的用户。
如果两个同时存在可能造成关节抖动
当两个都不存在时，坐标树生成不了 机器人模型会显示异常
robot_state_publisher 一直发布初始关节位置信息
而robot_state_publisher_gui会发布用户在GUI界面上设置的关节位置信息 
两个消息都会被订阅 这样就会造成关节抖动 

"""
