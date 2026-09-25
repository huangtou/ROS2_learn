import rclpy
from rclpy.node import Node
from student_interfaces.msg import Student

"""  
    需求：订阅发布方发布的消息，并输出到终端。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建订阅方；
            3-2.处理订阅到的消息。
        4.调用spin函数,并传入节点对象,
        5.释放资源。
"""

class StudentTalker(Node):
    def __init__(self):
        super().__init__('student_talker')
        self.get_logger().info('student_talker节点发布方创建！')
        # 创建发布方 参数：发送数据类型 话题名称 队列长度 返回值：发布方对象
        self.pub = self.create_publisher(Student, 'student', 10)
        # 创建定时器 参数 间隔事件 回调函数
 
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1s回调一次
        # 编号
        self.count = 0

    def timer_callback(self):
        msg = Student()
        msg.name = f'Student_{self.count}'
        msg.age = 20 + self.count
        msg.height = 1.70 + (self.count * 0.01)
        self.pub.publish(msg)
        self.get_logger().info(
            f'发布消息：name={msg.name}, age={msg.age}, height={msg.height:.2f}'
        )
        self.count += 1



def main():
    #初始化ros2客户端
    rclpy.init()

    #创建节点对象
    node = StudentTalker()
    #传入spin函数
    rclpy.spin(node)


    #释放ros2资源
    rclpy.shutdown()


if __name__ == '__main__':
    main()