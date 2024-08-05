from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    # Get the share directory of the package
    pkg_share = FindPackageShare(package='usf_robot_description').find('usf_robot_description')

    # Define the path to the URDF file
    urdf_file = os.path.join(pkg_share, 'urdf', 'usf_robot.urdf')
    
    # Declare arguments
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true'
    )
    
    # Define the robot description parameter
    robot_description = {'robot_description': open(urdf_file).read()}
    
    # Define the MoveIt Setup Assistant node
    moveit_setup_assistant_node = Node(
        package='moveit_setup_assistant',
        executable='moveit_setup_assistant',
        name='moveit_setup_assistant',
        output='screen',
        parameters=[robot_description]
    )
    
    return LaunchDescription([
        declare_use_sim_time,
        moveit_setup_assistant_node
    ])
