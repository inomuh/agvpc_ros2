from agv_service.srv import DataService

import rclpy
import time
import os.path

def main(args=None):
    rclpy.init(args=args)
    datetime_object = time.strftime("%Y%m%d-%H%M%S")
    service_directory = os.path.abspath(os.path.dirname(__file__))
    file_name = os.path.abspath(os.path.join(service_directory, '../../../../../../src/agvpc_ros2/agv_data_transfer_service/map/'+datetime_object+'map.pgm'))

    node = rclpy.create_node('data_transfer_client')
    cli = node.create_client(DataService, 'data_service')

    req = DataService.Request()
    req.istenen = 5
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')
        
    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
  
        with open(file_name, "wb") as binary_file:    
            newFileByteArray = bytearray(future.result().sonuc)
            binary_file.write(newFileByteArray)

        node.get_logger().info(
            'Data Servis:  %d   ' %
            (req.istenen))    #(req.a, req.b, future.result().sum)
    else:
        node.get_logger().info('Service call failed %r' % (future.exception(),))

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
