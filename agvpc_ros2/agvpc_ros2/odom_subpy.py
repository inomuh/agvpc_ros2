'''Odometri Abonesi
Navigation mesaj tipinde görev durumunu dinlemek için yazılmış düğümdür.
nav_msgs mesaj dosyasındaki Odometry.msg mesaj tipini kullanmaktadır.
Mesaj tipinin içerisi :

std_msgs/Header header
string child_frame_id
geometry_msgs/PoseWithCovariance pose
geometry_msgs/TwistWithCovariance twist

Abone olunan topik agv"robot_id"/odom şeklindedir.
'''

import sys
import rclpy																				#Python kütüphanelerinin çağırılması için kullanılır.

from nav_msgs.msg import Odometry															#Abone olunan topik için mesaj tipinin tanımlanması için kullanılır.

robot_id=input('Robot Numarası Giriniz: ')													#Seçilen robot id'sine göre abone olunacak topiğin oluşturulması için kullanıcıya(otomatik olarak sunucuya) robotun numarası sorulur.
robot_id_name='agv'+robot_id+'/odom'														#Böylece robot_id_name değişkeni için "agv1/odom" gibi topik ismi oluşturulur.

def chatter_callback(msg):
    global node
    message_data='{"Konum":{\n'+'"Child Frame Id":"'+str(msg.header.stamp.sec)+'",\n'+'"Pose":{\n'+'"Pose":{\n'+'"Position":{\n'+'"x":"'+str(msg.pose.pose.position.x)+'",\n'+'"y":"'+str(msg.pose.pose.position.y)+'",\n'+'"z":"'+str(msg.pose.pose.position.z)+'"\n'+'},'+'"Orientation":{'+'"x":"'+str(msg.pose.pose.orientation.x)+'",\n'+'"y":"'+str(msg.pose.pose.orientation.y)+'",\n'+'"z":"'+str(msg.pose.pose.orientation.z)+'",\n'+'"w":"'+str(msg.pose.pose.orientation.w)+'"\n'+'}\n'+'},\n'+'"Covariance":'+str(msg.pose.covariance)+'\n'+'},\n'+'"Twist":{'+'"Twist":{'+'"Linear":{'+'"x":"'+str(msg.twist.twist.linear.x)+'",\n'+'"y":"'+str(msg.twist.twist.linear.y)+'",\n'+'"z":"'+str(msg.twist.twist.linear.z)+'"\n'+'},\n'+'"Angular":{\n'+'"x":"'+str(msg.twist.twist.angular.x)+'",\n'+'"y":"'+str(msg.twist.twist.angular.y)+'",\n'+'"z":"'+str(msg.twist.twist.angular.z)+'"\n'+'}\n'+'},\n'+'"Covariance":'+str(msg.twist.covariance)+'\n'+'}\n'+'}\n'+'}\n'
    '''
    JSON DATA
    message_data='{"Konum":{\n'
								+'"Child Frame Id":"'+str(msg.child_frame_id)
								+'",\n'
								+'"Pose":{\n'
								+'"Pose":{\n'
								+'"Position":{\n'
								+'"x":"'+str(msg.pose.pose.position.x)+'",\n'
								+'"y":"'+str(msg.pose.pose.position.y)+'",\n'
								+'"z":"'+str(msg.pose.pose.position.z)+'"\n'
								+'},'
								+'"Orientation":{'
								+'"x":"'+str(msg.pose.pose.orientation.x)+'",\n'
								+'"y":"'+str(msg.pose.pose.orientation.y)+'",\n'
								+'"z":"'+str(msg.pose.pose.orientation.z)+'",\n'
								+'"w":"'+str(msg.pose.pose.orientation.w)+'"\n'
								+'}\n'
								+'},\n'
								+'"Covariance":'+str(msg.pose.covariance)+'\n'
								+'},\n'
								+'"Twist":{'
								+'"Twist":{'
								+'"Linear":{'
								+'"x":"'+str(msg.twist.twist.linear.x)+'",\n'
								+'"y":"'+str(msg.twist.twist.linear.y)+'",\n'
								+'"z":"'+str(msg.twist.twist.linear.z)+'"\n'
								+'},\n'
								+'"Angular":{\n'
								+'"x":"'+str(msg.twist.twist.angular.x)+'",\n'
								+'"y":"'+str(msg.twist.twist.angular.y)+'",\n'
								+'"z":"'+str(msg.twist.twist.angular.z)+'"\n'
								+'}\n'
								+'},\n'
								+'"Covariance":'+str(msg.twist.covariance)+'\n'+'}\n'+'}\n'+'}\n'
    
    '''
    print(message_data)
    
def main(args=None):
    global node
    rclpy.init(args=args)
    node = rclpy.create_node('python_subscriber_odom_subs')

    subscription = node.create_subscription(Odometry, robot_id_name, chatter_callback)

    while rclpy.ok():
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
