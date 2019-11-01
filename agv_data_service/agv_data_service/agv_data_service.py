from agv_service.srv import AgvDataServicev1

import rclpy
import xml.etree.ElementTree as ET
import os.path

g_node = None

def agv_data_callback(request, response):
    global g_node
    service_directory = os.path.abspath(os.path.dirname(__file__))
    text_name = os.path.abspath(os.path.join(service_directory, '../../../../../../src/agvpc_ros2/agv_data_service/data/agv_data_'+request.istek+'.xml'))
    tree = ET.parse(text_name)    
    root = tree.getroot()
    child_size = [0] * len(root)
    dataJson = "{" + "\"" + "robot bilgisi" + "\"" + ":" + "{"

    for index in range(len(root)):
        child_size[index] = len(root[index])
         
    for index in range(len(root)):

        if(len(root[index]) == 0):
            dataJson = dataJson + "\"" + root[index].tag + "\"" + ":"
            dataJson = dataJson + "\"" + root[index].text + "\""
        else:
            dataJson = dataJson + "\"" + root[index].tag + "\"" + ":" + "{"
            for iindex in range(child_size[index]):
                dataJson = dataJson + "\"" +root[index][iindex].tag + "\"" + ":" \
                        + "\"" + root[index][iindex].text + "\""
                if iindex != child_size[index]-1:
                    dataJson = dataJson + "," 
            dataJson = dataJson + "}"
        if index != len(root)-1:
            dataJson = dataJson + "," 
    dataJson = dataJson + "}" + "}"
    print(dataJson)    
    response.cevap = dataJson
    return response


def main(args=None):
    global g_node
    rclpy.init(args=args)

    g_node = rclpy.create_node('agv_data_service')

    srv = g_node.create_service(AgvDataServicev1, 'agv_data_service', agv_data_callback)


    while rclpy.ok():
        rclpy.spin_once(g_node)

    g_node.destroy_service(srv)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
