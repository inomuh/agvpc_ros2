import rclpy
from rclpy.node import Node
#Abone olunan topik için mesaj tipinin tanımlanması için kullanılır.
from nav_msgs.msg import Odometry				
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid

class Konum(Node):
	#robot_id=input('Robot Numarası Giriniz: ')
	
	def __init__(self,robot_id):
		super(Konum,self).__init__('konum')
		self.robot_id = robot_id
		self.topicname='/odom'
		self.topic='agv'+str(self.robot_id)+self.topicname
#		self.conn = DbConnect()
		self.subscription = self.create_subscription(
			Odometry,
			self.topic,
			self.listener_callback)
		self.subscription  # prevent unused variable warning
	def listener_callback(self, msg):
		message_data='{"Konum":{\n'+'"Child Frame Id":"'+str(msg.child_frame_id)+'",\n'+'"Pose":{\n'+'"Pose":{\n'+'"Position":{\n'+'"x":"'+str(msg.pose.pose.position.x)+'",\n'+'"y":"'+str(msg.pose.pose.position.y)+'",\n'+'"z":"'+str(msg.pose.pose.position.z)+'"\n'+'},'+'"Orientation":{'+'"x":"'+str(msg.pose.pose.orientation.x)+'",\n'+'"y":"'+str(msg.pose.pose.orientation.y)+'",\n'+'"z":"'+str(msg.pose.pose.orientation.z)+'",\n'+'"w":"'+str(msg.pose.pose.orientation.w)+'"\n'+'}\n'+'},\n'+'"Covariance":'+str(msg.pose.covariance)+'\n'+'},\n'+'"Twist":{'+'"Twist":{'+'"Linear":{'+'"x":"'+str(msg.twist.twist.linear.x)+'",\n'+'"y":"'+str(msg.twist.twist.linear.y)+'",\n'+'"z":"'+str(msg.twist.twist.linear.z)+'"\n'+'},\n'+'"Angular":{\n'+'"x":"'+str(msg.twist.twist.angular.x)+'",\n'+'"y":"'+str(msg.twist.twist.angular.y)+'",\n'+'"z":"'+str(msg.twist.twist.angular.z)+'"\n'+'}\n'+'},\n'+'"Covariance":'+str(msg.twist.covariance)+'\n'+'}\n'+'}\n'+'}\n'
 #Yayımcıdan gelen mesajı JSON tipine dönüştürmek için message_data string'i kullanılır.
		print(message_data)	
#		self.conn.exec_query("INSERT INTO PrdPublishData VALUES(1,'2018-06-07 17:41:40.323','" + message_data + "'," + self.robot_id + ")")

"""------------------------------------------------------------------------------------------------------"""

class Vel(Node):
	#robot_id=input('Robot Numarası Giriniz: ')
	
	def __init__(self,robot_id):
		super(Hiz,self).__init__('hiz_class')
		self.robot_id = robot_id
		self.topicname='/cmd_vel'
		self.topic='agv'+str(self.robot_id)+self.topicname
#		self.conn = DbConnect()
		self.subscription = self.create_subscription(
			Twist,
			self.topic,
			self.listener_callback)
		self.subscription  # prevent unused variable warning
	def listener_callback(self, msg):
		message_data='{"Hız":{\n"Linear":{\n'+'"x":"'+str(msg.linear.x)+'",\n'+'"y":"'+str(msg.linear.y)+'",\n'+'"z":"'+str(msg.linear.z)+'"\n'+'}\n,'+'"Angular":{\n' +'"x":"'+str(msg.angular.x)+'",\n'+'"y":"'+str(msg.angular.y)+'",\n'+'"z":"'+str(msg.angular.z)+'"\n'+'}\n'+'}\n'+'}\n'
		print(message_data)	
#		self.conn.exec_query("INSERT INTO PrdPublishData VALUES(1,'2018-06-07 17:41:40.323','" + message_data + "'," + self.robot_id + ")")

"""------------------------------------------------------------------------------------------------------"""
class OccupancyGridMap(Node):
	#robot_id=input('Robot Numarası Giriniz: ')
	
	def __init__(self,robot_id):
		super(OccupancyGridMap,self).__init__('occupancy_grid_map')
		self.robot_id = robot_id
		self.topicname='/map'
		self.topic='agv'+str(self.robot_id)+self.topicname
#		self.conn = DbConnect()
		self.subscription = self.create_subscription(
			OccupancyGrid,
			self.topic,
			self.listener_callback)
		self.subscription  # prevent unused variable warning
	def listener_callback(self, msg):
		message_data='{"Info":{\n'+'"Width":"'+str(msg.info.width)+'",\n'+'"Height":"'+str(msg.info.height)+'",\n'+'"Resolution":"'+str(msg.info.resolution)+'",\n'+'"Origin":{\n'+'"Position":{'+'"x":"'+str(msg.info.origin.position.x)+'",\n'+'"y":"'+str(msg.info.origin.position.y)+'",\n'+'"z":"'+str(msg.info.origin.position.z)+'"\n'+'},\n'+'"Orientation":{'+'"x":"'+str(msg.info.origin.orientation.x)+'",\n'+'"y":"'+str(msg.info.origin.orientation.y)+'",\n'+'"z":"'+str(msg.info.origin.orientation.z)+'"\n'+'}\n'+'}\n'+'},\n'+'"Data":'+str(msg.data)+'\n'+'}'
		print(message_data)	
#		self.conn.exec_query("INSERT INTO PrdPublishData VALUES(1,'2018-06-07 17:41:40.323','" + message_data + "'," + self.robot_id + ")")

"""------------------------------------------------------------------------------------------------------"""


