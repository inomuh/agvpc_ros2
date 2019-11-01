import rclpy
from rclpy.node import Node

from agv_msgs.msg import TaskCom


class TaskComClass(Node):

    def __init__(self):
        super().__init__('status')
        self.i = 0
        self.product_name='B'
        self.product_count = 1
        self.duty = 1
        self.status = 0        
        self.sub = self.create_subscription(TaskCom, 'OTA_status', self.task_callback)                
        self.pub = self.create_publisher(TaskCom, 'rk_hmi_status')
        timer_period = 1.0
        self.tmr = self.create_timer(timer_period, self.timer_callback)

    def task_callback(self, msg):
        self.product_name = msg.product_name
        self.product_count = msg.product_count
        self.duty = msg.duty
        self.status = msg.status
        print('product_countl',self.product_count)
        
    def timer_callback(self):
        msg = TaskCom()
        msg.station_id = 12345
        msg.product_name = self.product_name
        msg.product_count = self.product_count
        msg.duty = self.duty
        msg.status = 1
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = TaskComClass()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
