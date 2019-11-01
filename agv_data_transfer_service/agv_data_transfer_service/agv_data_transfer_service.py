from agv_service.srv import DataService

import rclpy
import os.path

g_node = None

def data_service_callback(request, response):
	global g_node
	service_directory = os.path.abspath(os.path.dirname(__file__))
	text_name = os.path.abspath(os.path.join(service_directory, '../../../../../../src/agvpc_ros2/agv_data_transfer_service/map/foto.pgm'))
	binary_file = open(text_name, "rb")
	binary_file.seek(0)
	by = binary_file.read()
	file_array = []
	for b in by:
		file_array.append(b)
	response.sonuc = file_array
	print("data gönderildi.")
	g_node.get_logger().info(
	    'Incoming request\nIstenen: %d ' % (request.istenen))		#'Incoming request\na: %d b: %d' % (request.a, request.b))

	return response


def main(args=None):
    global g_node
    rclpy.init(args=args)

    g_node = rclpy.create_node('data_transfer_service')

    srv = g_node.create_service(DataService, 'data_service', data_service_callback)
    while rclpy.ok():
        rclpy.spin_once(g_node)

    # Destroy the service attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    g_node.destroy_service(srv)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
