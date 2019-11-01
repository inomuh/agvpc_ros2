
import rclpy
from rclpy.node import Node
import time
from agv_msgs.msg import TaskCom

agv_st = 0

class Listener(Node):

    def __init__(self):
        super().__init__('robot_kolu')
        self.sub = self.create_subscription(TaskCom, '/OTA_status', self.agv_callback)
        print("agv_status %d" % agv_st)
        self.pub = self.create_publisher(TaskCom, '/rk_hmi_status')


    def agv_callback(self, msg):
        self.get_logger().info('I heard: [%d]' % msg.status)
        agv_st = msg.status
        print("agv_status %d" % agv_st)
        if(agv_st == 1):
            print("burada")
            timer_period = 1.0
            self.tmr = self.create_timer(timer_period, self.timer_callback)
        else:
            print("agv_status_else %d" % agv_st)

    def timer_callback(self):
        time.sleep(10)
        msgpub = TaskCom()
        msgpub.status = 1
        print('Publishing: "{%d}"'% msgpub.status)
        self.pub.publish(msgpub)


def main(args=None):
    rclpy.init(args=args)

    node = Listener()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


