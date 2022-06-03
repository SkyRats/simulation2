import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    simulation_pkg_dig = get_package_share_directory('simulation2')
    world = os.path.join(simulation_pkg_dig, 'worlds', 'aruco.world')


    open_gazebo = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('simulation2'), 'launch'),
         '/gazebo.launch.py']),
      launch_arguments={'world': world}.items(),
      )
    put_drone = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('simulation2'), 'launch'),
         '/spawn_drone.launch.py']),
      #launch_arguments={'target_frame': 'carrot1'}.items(),
      )
    return LaunchDescription([
      open_gazebo,
      put_drone
    ])