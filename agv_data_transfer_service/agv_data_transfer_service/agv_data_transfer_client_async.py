from agv_service.srv import DataService

import rclpy
import time
import os.path

def main(args=None):
	rclpy.init(args=args)
	
	datetime_object = time.strftime("%Y%m%d-%H%M%S")
	service_directory = os.path.abspath(os.path.dirname(__file__))
	file_name = os.path.abspath(os.path.join(service_directory, '../../../../../../src/agvpc_ros2/agv_data_transfer_service/map/'+datetime_object+'map.pgm'))
	
	node = rclpy.create_node('agv_data_transfer_client')
	cli = node.create_client(DataService, 'data_service')
	req = DataService.Request()
	req.istenen = 5
	while not cli.wait_for_service(timeout_sec=1.0):
		node.get_logger().info('service not available, waiting again...')
	future = cli.call_async(req)
	while rclpy.ok():
		rclpy.spin_once(node)
		if future.done():
			if future.result() is not None:
				node.get_logger().info('Result %d' % req.istenen)
				with open(file_name, "wb") as binary_file:    
					newFileByteArray = bytearray(future.result().sonuc)
					binary_file.write(newFileByteArray)
			else:
				node.get_logger().info('Service call failed %r' % (future.exception(),))
			break

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
    main()
