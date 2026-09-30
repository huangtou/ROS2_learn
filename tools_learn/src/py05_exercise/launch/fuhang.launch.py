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

    #1 获取参数
    escort_back=DeclareLaunchArgument(name="escort_back",default_value="escort_back")
    escort_right=DeclareLaunchArgument(name="escort_right",default_value="escort_right")
    escort_lift=DeclareLaunchArgument(name="escort_lift",default_value="escort_lift")

    #创建turtlesim_node节点 并生成新乌龟
    master=Node(
        package="turtlesim",
        executable="turtlesim_node",
    )

    spawn_back=Node(
        package="py05_exercise",
        executable="exer01_spawn_py",
        name="spawn_back",
        parameters=[{
                    "x":2.5,
                    "y":5.0,
                    'name':LaunchConfiguration("escort_back"),
                }]
    )

    spawn_right=Node(
        package="py05_exercise",
        executable="exer01_spawn_py",
        name="spawn_right",
        parameters=[{
                    "x":5.0,
                    "y":2.5,
                    'name':LaunchConfiguration("escort_right"),
                }]
    )

    spawn_lift=Node(
        package="py05_exercise",
        executable="exer01_spawn_py",
        name="spawn_lift",
        parameters=[{
                    "x":5.0,
                    "y":7.5,
                    'name':LaunchConfiguration("escort_lift"),
                }]
    )




    #发布坐标变换
    tf1_word=Node(
        package="py05_exercise",
        executable="exer02_tf_broadcaster_py",
        name="tf1",
    )

    tf2_back=Node(
        package="py05_exercise",
        executable="exer02_tf_broadcaster_py",
        name="tf2",
        parameters=[{
                    'turtle':LaunchConfiguration('escort_back'),
                }]
    )

    tf2_right=Node(
        package="py05_exercise",
        executable="exer02_tf_broadcaster_py",
        name="tf3",
        parameters=[{
                    'turtle':LaunchConfiguration('escort_right'),
                }]
    )

    tf2_lift=Node(
        package="py05_exercise",
        executable="exer02_tf_broadcaster_py",
        name="tf4",
        parameters=[{
                    'turtle':LaunchConfiguration('escort_lift'),
                }]
    )


    #目标点相对于乌龟坐标系的坐标变换 静态广播
    esxort_goal_back=Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="esxort_goal_back",
        arguments=["--frame-id","turtle1","--child-frame-id","esxort_goal_back","--x","-1.5",]
    )

    escort_goal_right=Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="escort_goal_right",
        arguments=["--frame-id","turtle1","--child-frame-id","escort_goal_right","--y","-1.5",]
    )

    escort_goal_lift=Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="escort_goal_lift",
        arguments=["--frame-id","turtle1","--child-frame-id","escort_goal_lift","--y","1.5",]
    )



    #监听坐标变换
    listener_esxort_back=Node(
        package="py05_exercise",
        executable="exer03_tf_listener_py",
        name="listener_esxort_back",
        parameters=[{"father_frame":LaunchConfiguration("escort_back"),"child_frame":"esxort_goal_back"}]
    )

    listener_esxort_right=Node(
        package="py05_exercise",
        executable="exer03_tf_listener_py",
        name="listener_esxort_right",
        parameters=[{"father_frame":LaunchConfiguration("escort_right"),"child_frame":"escort_goal_right"}]
    )

    listener_esxort_lift=Node(
        package="py05_exercise",
        executable="exer03_tf_listener_py",
        name="listener_esxort_lift",
        parameters=[{"father_frame":LaunchConfiguration("escort_lift"),"child_frame":"escort_goal_lift"}]
    )


   






    return LaunchDescription([
        escort_back,
        escort_right,
        escort_lift,
        master,
        spawn_back,
        spawn_right,
        spawn_lift,
        tf1_word,
        tf2_back,
        tf2_right,
        tf2_lift,
        esxort_goal_back,
        escort_goal_right,
        escort_goal_lift,
        listener_esxort_back,
        listener_esxort_right,
        listener_esxort_lift,
    ])