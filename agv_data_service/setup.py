from setuptools import setup

package_name = 'agv_data_service'

setup(
 name=package_name,
 version='0.0.0',
 packages=[package_name],
 data_files=[
     ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
     ('share/' + package_name, ['package.xml']),
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
             'agv_data_client = agv_data_service.agv_data_client:main',
             'agv_data_service = agv_data_service.agv_data_service:main',
     ],
   },
)
