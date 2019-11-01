import rclpy
from rclpy.node import Node

from agv_msgs.msg import TaskRequest


class TaskRequestClass(Node):

    def __init__(self):
        super().__init__('talker')
        self.i = 0
        self.pub = self.create_publisher(TaskRequest, 'hmi_task')
        timer_period = 1.0
        self.tmr = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = TaskRequest()
        msg.station_id = 12345
        msg.product_name = 'A'
        msg.product_count = 10
        msg.duty = 1
        msg.task_priority = 1
        msg.delivery_time = '2019-10-30'
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = TaskRequestClass()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
