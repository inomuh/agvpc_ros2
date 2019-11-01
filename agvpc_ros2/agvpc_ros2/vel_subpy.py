'''Görev Durum Abonesi
Geometry mesaj tipinde görev durumunu dinlemek için yazılmış düğümdür.
geometry_msgs mesaj dosyasındaki Twist.msg mesaj tipini kullanmaktadır.
Mesaj tipinin içerisi :

Vector3  linear
Vector3  angular

Abone olunan topik agv"robot_id"/cmd_vel şeklindedir.
'''

import sys
import rclpy																		#Python kütüphanelerinin çağırılması için kullanılır.

from geometry_msgs.msg import Twist													#Abone olunan topik için mesaj tipinin tanımlanması için kullanılır.

robot_id=input('Robot Numarası Giriniz: ')											#Seçilen robot id'sine göre abone olunacak topiğin oluşturulması için kullanıcıya(otomatik olarak sunucuya) robotun numarası sorulur.
robot_id_name='agv'+robot_id+'/cmd_vel'												#Böylece robot_id_name değişkeni için "agv1/gorev_durumu" gibi topik ismi oluşturulur.

def chatter_callback(msg):
    global node
    message_data='{"Velocity":{\n"Linear":{\n'+'"x":"'+str(msg.linear.x)+'",\n'+'"y":"'+str(msg.linear.y)+'",\n'+'"z":"'+str(msg.linear.z)+'"\n'+'}\n,'+'"Angular":{\n' +'"x":"'+str(msg.angular.x)+'",\n'+'"y":"'+str(msg.angular.y)+'",\n'+'"z":"'+str(msg.angular.z)+'"\n'+'}\n'+'}\n'+'}\n'
    print(message_data)
    
    '''
    JSON DATA
    message_data='{"Hız":{\n"Linear":{\n'+'"x":"'+str(msg.linear.x)+'",\n'
										 +'"y":"'+str(msg.linear.y)+'",\n'
										 +'"z":"'+str(msg.linear.z)+'"\n'+'}\n,'
						  +'"Angular":{\n' 
										 +'"x":"'+str(msg.angular.x)+'",\n'
										 +'"y":"'+str(msg.angular.y)+'",\n'
										 +'"z":"'+str(msg.angular.z)+'"\n'
										 +'}\n'
										 +'}\n'
										 +'}\n'

    '''


def main(args=None):
    global node
    rclpy.init(args=args)
    node = rclpy.create_node('python_subscriber_hiz_sub')

    subscription = node.create_subscription(Twist, robot_id_name, chatter_callback)

    while rclpy.ok():
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
