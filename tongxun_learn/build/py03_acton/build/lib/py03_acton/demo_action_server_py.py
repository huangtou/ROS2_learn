import rclpy
from rclpy.action import ActionServer, GoalResponse
from rclpy.node import Node
from student_interfaces.action import Progress
import sys
import time



#创建节点对象
class DemoActionsServer(Node):
    def __init__(self):
        super().__init__("my_action_Server_node")
        self.get_logger().info("服务端节点创建成功")

        #创建服务端
        #参1：节点对象 参2:接口类型（参数类型） 参3：话题名称 参4：回调函数
        self.action_server=ActionServer(
            self,
            Progress,
            "progress",
            self.execute_callback,
            goal_callback=self.goal_callback
        )

    def goal_callback(self, goal_request):
        if goal_request.num < 0:
            self.get_logger().warning("拒绝负数目标")
            return GoalResponse.REJECT

        return GoalResponse.ACCEPT

    #创建回调函数 参1 节点对象 参2 目标句柄对象
    def execute_callback(self,goal_handle):
        #获取客户端传入的参数
        num=goal_handle.request.num
        #创建求和
        sum=0
        #创建求和
        for i in range(1,num+1):
            sum+=i
            #创建反馈对象
            feedback_msg=Progress.Feedback()
            #将进度赋值给反馈对象
            feedback_msg.progress=i/num
            #发送反馈
            goal_handle.publish_feedback(feedback_msg)
            #打印
            self.get_logger().info(f"反馈进度：{feedback_msg.progress*100}%")
            #休眠一会
            time.sleep(1)

        #相应结果
        goal_handle.succeed()#设置目标句柄状态为成功
        #创建响应对象
        result=Progress.Result()
        #将最终结果赋值给响应对象
        result.sum=sum

        self.get_logger().info(f"最终结果：{result.sum}")
        #返回响应对象
        return result


#创建客户端
def main():

    #初始化ros2
    rclpy.init()

    #创建节点对象
    server = DemoActionsServer()
    #传入spin
    rclpy.spin(server)

    #释放资源
    rclpy.shutdown()
    pass


if __name__ == '__main__':
    main()