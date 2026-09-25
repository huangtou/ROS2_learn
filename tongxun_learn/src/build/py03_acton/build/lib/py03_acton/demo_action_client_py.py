import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from student_interfaces.action import Progress
import sys
from rclpy.logging import get_logger



#创建节点对象
class DemoActionClient(Node):
    def __init__(self):
        super().__init__("my_action_client_node")
        self.get_logger().info("客户端节点创建成功")

        #创建客户端 参1 节点 参2 参数类型 参3 话题名称
        self.action_client=ActionClient(
            self,
            Progress,
            "progress"
        )

        #发送请求
    def send_goal(self,num):

        #连接服务段
        while not self.action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info("等待服务端连接...")

        goal=Progress.Goal()
        goal.num=num
        #发送请求 参数1 目标值 参2 回调函数
        self.future=self.action_client.send_goal_async(goal,self.feedback_callback)

        #当执行完毕后调用 判断输入是否合法
        self.future.add_done_callback(self.goal_response_callback)

    #参数1 节点 参数2 反馈对象
    def feedback_callback(self,feedback_msg):
        feed_back=feedback_msg.feedback.progress#获取联系反馈数据
        self.get_logger().info(f"反馈进度：{feed_back*100}%")

    def goal_response_callback(self,future):
        #获取目标句柄
        goal_handle=future.result() 
        #判断目标句柄是否被接受
        if not goal_handle.accepted:
            self.get_logger().info("目标被拒绝")
            return
        self.get_logger().info("目标被接受")

        #获取最终结果
        self.result_future=goal_handle.get_result_async()
        self.result_future.add_done_callback(self.get_result_callback)

    #处理最终响应
    def get_result_callback(self,future):
        result=future.result().result
        self.get_logger().info(f"最终结果：{result.sum}")





       

#创建客户端
def main():

    #动态解析传入的参数
    if len(sys.argv) != 2:
        get_logger('rclpy').error("参数错误！请传入一个整型数据")
        return

    #初始化ros2
    rclpy.init()
    #创建节点对象
    client = DemoActionClient()
    client.send_goal(int(sys.argv[1]))
    #传入spin
    rclpy.spin(client)
    #释放资源
    rclpy.shutdown()
    pass


if __name__ == '__main__':
    main()