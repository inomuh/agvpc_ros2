import sys
import rclpy																	#Python kütüphanelerinin çağırılması için kullanılır.
import json									#Abone olunan topik için mesaj tipinin tanımlanması için kullanılır.
from std_msgs.msg import String

def chatter_callback(msg):
    global node
    gorev_sunucu=msg.data
    print(gorev_sunucu)
    gg = json.loads(gorev_sunucu)
    for i in range(len(gg["plan"])):
        robotId = gg["plan"][i]["robotID"]
        robotEquipmentID = gg["plan"][i]["robotEquipmentID"]
        #print("%d %d\n" % (robotId,robotEquipmentID))
        robotTaskList = gg["plan"][i]["taskList"]
        for y in range(len(gg["plan"][i]["taskList"])):
            print(y)
            robotTaskId = gg["plan"][i]["taskList"][y]["id"]
            robotTaskWorkBench = gg["plan"][i]["taskList"][y]["workbenchID"]
            robotTaskStationId = gg["plan"][i]["taskList"][y]["stationID"]
            robotTaskDuty = gg["plan"][i]["taskList"][y]["duty"]
            robotTaskProductName = gg["plan"][i]["taskList"][y]["productName"]
            robotTaskProductCount = gg["plan"][i]["taskList"][y]["productCount"]
            print("%d %d %d %s %s %d\n" %(robotTaskId,robotTaskWorkBench,robotTaskStationId,robotTaskDuty,robotTaskProductName,robotTaskProductCount))
            print("***********************")
            for z in range(len(gg["plan"][i]["taskList"][y]["route"])):
                print(z)
                if len(gg["plan"][i]["taskList"][y]["route"][z]["tags"]) == 3:
                    robotTaskRouteTagType = gg["plan"][i]["taskList"][y]["route"][z]["tags"]["type"]
                    robotTaskRouteTagTypeCode = gg["plan"][i]["taskList"][y]["route"][z]["tags"]["type_code"]
                    robotTaskRouteTagTypeDef = gg["plan"][i]["taskList"][y]["route"][z]["tags"]["type_definition"]
                    robotTaskRouteX = gg["plan"][i]["taskList"][y]["route"][z]["x"]
                    robotTaskRouteY = gg["plan"][i]["taskList"][y]["route"][z]["y"]
                    robotTaskRouteXYId = gg["plan"][i]["taskList"][y]["route"][z]["id"]
                    waypoint = [robotTaskRouteTagType,robotTaskRouteTagTypeCode,robotTaskRouteTagTypeDef,robotTaskRouteX,robotTaskRouteY,robotTaskRouteXYId]
                    print(waypoint)
                    #print("%s %s %s %f %f %d\n" %(robotTaskRouteTagType,robotTaskRouteTagTypeCode,robotTaskRouteTagTypeDef,robotTaskRouteX,robotTaskRouteY,robotTaskRouteXYId))
                if len(gg["plan"][i]["taskList"][y]["route"][z]["tags"]) == 4:
                    robotTaskRouteTagIntersection = gg["plan"][i]["taskList"][y]["route"][z]["tags"]["intersection"]
                    robotTaskRouteTagType = gg["plan"][i]["taskList"][y]["route"][z]["tags"]["type"]
                    robotTaskRouteTagTypeCode = gg["plan"][i]["taskList"][y]["route"][z]["tags"]["type_code"]
                    robotTaskRouteTagTypeDef = gg["plan"][i]["taskList"][y]["route"][z]["tags"]["type_definition"]
                    robotTaskRouteX = gg["plan"][i]["taskList"][y]["route"][z]["x"]
                    robotTaskRouteY = gg["plan"][i]["taskList"][y]["route"][z]["y"]
                    robotTaskRouteXYId = gg["plan"][i]["taskList"][y]["route"][z]["id"]
                    #print("%s %s %s %s %f %f %d\n" %(robotTaskRouteTagIntersection,robotTaskRouteTagType,robotTaskRouteTagTypeCode,robotTaskRouteTagTypeDef,robotTaskRouteX,robotTaskRouteY,robotTaskRouteXYId))
                    waypoint = [robotTaskRouteTagType,robotTaskRouteTagTypeCode,robotTaskRouteTagTypeDef,robotTaskRouteX,robotTaskRouteY,robotTaskRouteXYId]
                    print(waypoint)

def main(args=None):
    global node
    rclpy.init(args=args)
    node = rclpy.create_node('python_subscriber_gorev')

    subscription = node.create_subscription(String, "task", chatter_callback)
    subscription  # prevent unused variable warning

    while rclpy.ok():
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
