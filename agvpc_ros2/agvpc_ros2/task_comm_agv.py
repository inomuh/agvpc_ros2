import rclpy
from rclpy.node import Node

from agv_msgs.msg import TaskCom

class OtaTaskComClass(Node):

    def __init__(self):
        super().__init__('ota_status')
        self.i = 0
        self.pub = self.create_publisher(TaskCom, 'OTA_status')
        timer_period = 1.0
        self.tmr = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = TaskCom()
        msg.station_id = 1
        msg.product_name = 'A'
        msg.product_count = 10
        msg.duty = 0
        msg.status = 1
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = OtaTaskComClass()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
