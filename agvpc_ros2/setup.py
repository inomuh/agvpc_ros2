import os
from glob import glob
from setuptools import setup

package_name = 'agvpc_ros2'

setup(
 name=package_name,
 version='0.0.0',
 packages=[package_name],
 data_files=[
     ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
     ('share/' + package_name, ['package.xml']),
     (os.path.join('share', package_name), glob('launch/start.launch.py'))
   ],
 install_requires=['setuptools'],
 zip_safe=True,
 maintainer='Didem Ozupek Tas',
 maintainer_email='didem.ozupektas@inovasyonmuhendislik.com',
 description='Server, HMI, Robot Arm communication',
 license='Apache License 2.0',
 tests_require=['pytest'],
 entry_points={
     'console_scripts': [
             'odom_subpy = agvpc_ros2.odom_subpy:main',
             'robot_kolu = agvpc_ros2.robot_kolu:main',
             'robot_map_subpy = agvpc_ros2.robot_map_subpy:main',
             'task_comm_hmi = agvpc_ros2.task_comm:main',
             'task_comm_agv = agvpc_ros2.task_comm_agv:main',
             'task_req = agvpc_ros2.task_req:main',
             'task_subpy = agvpc_ros2.task_subpy:main',
             'vel_subpy = agvpc_ros2.vel_subpy:main',
             'subscriber_classes = agvpc_ros2.subscriber_classes:main',
     ],
   },
)
