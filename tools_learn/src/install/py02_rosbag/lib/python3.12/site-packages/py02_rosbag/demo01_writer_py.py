"""  
  需求：录制 turtle_teleop_key 节点发布的速度指令。
  步骤：
    1.导包；
    2.初始化 ROS 客户端；
    3.定义节点类；
      3-1.创建写出对象；
      3-2.设置写出的目标文件、话题等参数；
      3-3.写出消息。
    4.调用 spin 函数，并传入对象；
    5.释放资源。

"""
# 1.导包；
import rclpy
from rclpy.node import Node
from rclpy.serialization import serialize_message#python对象不能直接写到数据库，用于转为二进制
from geometry_msgs.msg import Twist
import rosbag2_py
# 3.定义节点类；
class SimpleBagRecorder(Node):
    def __init__(self):
        super().__init__('simple_bag_recorder_py')
        # 3-1.创建rosbag写入器；创建了一个 rosbag 写入器，并保存到对象属性
        self.writer = rosbag2_py.SequentialWriter()
        # 3-2.设置写出的目标文件、话题等参数；
        storage_options = rosbag2_py._storage.StorageOptions(
            uri='my_bag_py',#存储文件夹位置
            storage_id='sqlite3')#存储格式
        converter_options = rosbag2_py._storage.ConverterOptions('cdr' , 'cdr')#序列格式转化 两个空格表示不需要转换 用默认格式
        #也可都为'cdr'，cdr 是 ROS 2 常见的消息序列化格式。
        self.writer.open(storage_options, converter_options)#打开写入器
        #按照指定的目录、数据库格式和序列化格式，打开一个用于写入的 rosbag。

        #描述要记录的话题
        topic_info = rosbag2_py._storage.TopicMetadata(
            id=0,#话题编号
            name='/turtle1/cmd_vel',#话题名称
            type='geometry_msgs/msg/Twist',#话题类型
            serialization_format='cdr')#表示消息使用 CDR 格式序列化。
        self.writer.create_topic(topic_info)#创建话题

        self.subscription = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.topic_callback,
            10)
        #self.subscription#将订阅者保存到对象属性中。这是常见写法，可以确保订阅对象在节点运行期间一直存在。
        #可以不用

    def topic_callback(self, msg):
        # 3-3.写出消息。
        self.writer.write(
            '/turtle1/cmd_vel',
            serialize_message(msg),
            self.get_clock().now().nanoseconds)


def main(args=None):
    # 2.初始化 ROS 客户端；
    rclpy.init(args=args)
    sbr = SimpleBagRecorder()
    try:
        # 4.调用 spin 函数，并传入对象；
        rclpy.spin(sbr)
    except KeyboardInterrupt:
        pass
    finally:
        # 5.释放资源。
        sbr.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()