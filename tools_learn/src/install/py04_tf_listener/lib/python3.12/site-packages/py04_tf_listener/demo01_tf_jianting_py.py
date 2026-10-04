"""  
  需求：订阅 laser 到 base_link 以及 camera 到 base_link 的坐标系关系，
       并生成 laser 到 camera 的坐标变换。
  步骤：
    1.导包；
    2.初始化 ROS 客户端；
    3.定义节点类；
      3-1.创建tf缓存对象指针；
      3-2.创建tf监听器；
      3-3.按照条件查找符合条件的坐标系并生成变换后的坐标帧。
    4.调用 spin 函数，并传入对象指针；
    5.释放资源。

"""
import rclpy
from rclpy.node import Node

from tf2_ros.buffer import Buffer#缓存对象
from tf2_ros.transform_listener import TransformListener#tf监听器


#创建节点
class TFListener(Node):
    def __init__(self):
        super().__init__("tf_lsitener_node")
        #创建tf缓存对象指针；
        self.buffer=Buffer()
        #创建tf监听器；
        self.listener=TransformListener(self.buffer,self)

        #创建定时器
        self.timer=self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):

        #判断是否可以转换
        if self.buffer.can_transform("camera","laser",rclpy.time.Time()):
            self.get_logger().info("可以转换")
        #实现转换            #新生成的关系的 父坐标系 子坐标系 时刻（一般为0 既最新时刻的）
            trans=self.buffer.lookup_transform("camera","laser",rclpy.time.Time())#查找laser到camera的坐标变换 如果buffer为0会报错 上面判断是否可以转换          
            self.get_logger().info("转换后数据")
            self.get_logger().info("父级坐标系id:%s"%trans.header.frame_id)
            self.get_logger().info("子级坐标系id:%s"%trans.child_frame_id)
            self.get_logger().info("坐标变换关系:平移:x=%.2f,y=%.2f,z=%.2f"%(trans.transform.translation.x,trans.transform.translation.y,trans.transform.translation.z))
            self.get_logger().info("坐标变换关系:旋转:x=%.2f,y=%.2f,z=%.2f,w=%.2f"%(trans.transform.rotation.x,trans.transform.rotation.y,trans.transform.rotation.z,trans.transform.rotation.w))
        else:
            self.get_logger().info("不可以转换")                                 





def main():
    rclpy.init()

    listener_node = TFListener()
    rclpy.spin(listener_node)


    rclpy.shutdown()
    pass


if __name__ == '__main__':
    main()
