import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'node_prefix',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), '_'],
            description='Prefix for node names'),
        launch_ros.actions.Node(
            package='agvpc_ros2', node_executable='task_comm_agv', output='screen',
            node_name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'task_comm_agv']),
        launch_ros.actions.Node(
            package='agvpc_ros2', node_executable='task_subpy', output='screen',
            node_name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'task_subpy']),
        launch_ros.actions.Node(
            package='agv_data_transfer_service', node_executable='agv_data_transfer_service', output='screen',
            node_name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'agv_data_transfer_service']),            
        launch_ros.actions.Node(
            package='agv_data_service', node_executable='agv_data_service', output='screen',
            node_name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'agv_data_service']),
    ])
