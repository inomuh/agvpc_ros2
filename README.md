# agvpc_ros2 packages used for communicate between hardwares which is used with agvpc_ros 

Dependencies:

Install Ros Kinetic, Ros2 Crystal, agvpc_ros to use agvpc_ros2 packages.

After git clone to your <ROS2_WORKSPACE_NAME>/src cut the ros1_bridge package to <another folder>. 

$ cd <ROS2_WORKSPACE_NAME>

$ colcon build --symlink-install

To use agv_msgs with ROS1 and ROS2 via ros1_bridge dynamic_bridge, we change the ros1_bridge package's CMakeLists.txt. You have to do following steps to use agv_msgs between ROS1 and ROS2.

$ source /opt/ros/<ROS_VERSION>/setup.bash

$ . ~/<ROS2_VERSION>/install/local_setup.bash

$ source ~/<ROS_WORKSPACE_NAME>/devel/setup.bash

$ . ~/<ROS2_WORKSPACE_NAME>/install/local_setup.bash

$ cd ~/<ROS2_VERSION>

$ rm -rf build/ros1_bridge

$ cp ~/<another folder>/ros1_bridge ~/<ROS2_VERSION>/src/ros2/
  
$ colcon build --symlink-install --packages-select ros1_bridge

$ . install/local_setup.bash

You must see agv_msgs custom messages as output of $ ros2 run ros1_bridge dynamic_bridge --print-pairs .

$ ros2 launch agvpc_ros2 start.launch.py
