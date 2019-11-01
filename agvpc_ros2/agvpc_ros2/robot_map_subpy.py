'''Map Abonesi
Navigation mesaj tipinde ilgi noktası durumunu dinlemek için yazılmış düğümdür.
nav_msgs mesaj dosyasındaki RobotId.msg mesaj tipini kullanmaktadır.
Mesaj tipinin içerisi :

std_msgs/Header header
MapMetaData info
int8[] data

Abone olunan topik agv"robot_id"/map şeklindedir.

'''
import sys
import rclpy																			#Python kütüphanelerinin çağırılması için kullanılır.

from nav_msgs.msg import OccupancyGrid													#Abone olunan topik için mesaj tipinin tanımlanması için kullanılır.
global i

robot_id=input('Robot Numarası Giriniz: ')												#Seçilen robot id'sine göre abone olunacak topiğin oluşturulması için kullanıcıya(otomatik olarak sunucuya) robotun numarası sorulur.
robot_id_name='agv'+robot_id+'/map'														#Böylece robot_id_name değişkeni için "agv1/map" gibi topik ismi oluşturulur.

def chatter_callback(msg):
    global node
    message_data='{"Info":{\n'+'"Width":"'+str(msg.info.width)+'",\n'+'"Height":"'+str(msg.info.height)+'",\n'+'"Resolution":"'+str(msg.info.resolution)+'",\n'+'"Origin":{\n'+'"Position":{'+'"x":"'+str(msg.info.origin.position.x)+'",\n'+'"y":"'+str(msg.info.origin.position.y)+'",\n'+'"z":"'+str(msg.info.origin.position.z)+'"\n'+'},\n'+'"Orientation":{'+'"x":"'+str(msg.info.origin.orientation.x)+'",\n'+'"y":"'+str(msg.info.origin.orientation.y)+'",\n'+'"z":"'+str(msg.info.origin.orientation.z)+'"\n'+'}\n'+'}\n'+'},\n'+'"Data":'+str(msg.data)+'\n'+'}'
    print(robot_id_name)
    '''
    JSON DATA
    message_data='{"Info":{\n'+'"Width":"'+str(msg.info.width)+'",\n'
							  +'"Height":"'+str(msg.info.height)+'",\n'
							  +'"Resolution":"'+str(msg.info.resolution)+'",\n'
							  +'"Origin":{\n'
							  +'"Position":{'
							  +'"x":"'+str(msg.info.origin.position.x)+'",\n'
							  +'"y":"'+str(msg.info.origin.position.y)+'",\n'
							  +'"z":"'+str(msg.info.origin.position.z)+'"\n'
							  +'},\n'
							  +'"Orientation":{'
							  +'"x":"'+str(msg.info.origin.orientation.x)+'",\n'
							  +'"y":"'+str(msg.info.origin.orientation.y)+'",\n'
							  +'"z":"'+str(msg.info.origin.orientation.z)+'"\n'
							  +'}\n'
							  +'}\n'
							  +'},\n'
							  +'"Data":'+str(msg.data)+'\n'
					+'}'
    
    '''
    
def main(args=None):
    global node
    rclpy.init(args=args)
    node = rclpy.create_node('python_subscriber_odom_subs')

    subscription = node.create_subscription(OccupancyGrid, robot_id_name, chatter_callback)
    subscription  # prevent unused variable warning

    while rclpy.ok():
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

