import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    open_gazebo = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('simulation2'), 'launch'),
         '/gazebo.launch.py']),
      launch_arguments={'world': LaunchConfiguration("world")}.items(),
      )
    put_drone = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('simulation2'), 'launch'),
         '/spawn_drone.launch.py']),
      launch_arguments={'sdf': LaunchConfiguration("drone")}.items(),
      )
    
    return LaunchDescription([
      DeclareLaunchArgument("world", default_value="empty.world"),
      open_gazebo,
      DeclareLaunchArgument("drone", default_value="iris"),
      put_drone
    ])