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
      launch_arguments={'sdf': LaunchConfiguration("drone"), 'x': LaunchConfiguration("x"), 'y': LaunchConfiguration("y"), 'z': LaunchConfiguration("z"), 'R': LaunchConfiguration("R"), 'P': LaunchConfiguration("P"), 'Y': LaunchConfiguration("Y")}.items(),
      )
    
    return LaunchDescription([
      DeclareLaunchArgument("world", default_value="empty.world"),
      open_gazebo,
      DeclareLaunchArgument("drone", default_value="iris"),
      DeclareLaunchArgument('x', default_value='0.0'),
      DeclareLaunchArgument('y', default_value='0.0'),
      DeclareLaunchArgument('z', default_value='1.0'),
      DeclareLaunchArgument('R', default_value='0.0'),
      DeclareLaunchArgument('P', default_value='0.0'),
      DeclareLaunchArgument('Y', default_value='0.0'),
      put_drone
    ])