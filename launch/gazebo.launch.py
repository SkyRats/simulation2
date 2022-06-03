#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    """Launch Gazebo with a drone running PX4 communicating over ROS 2."""
    HOME = os.environ.get('HOME')
    PX4_RUN_DIR = HOME + '/tmp/px4_run_dir'
    gazebo_launch_dir = os.path.join(get_package_share_directory('gazebo_ros'), 'launch')

    simulation_pkg_dig = get_package_share_directory('simulation2')
    world = os.path.join(simulation_pkg_dig, 'worlds', 'aruco.world')
    model = os.path.join(simulation_pkg_dig, 'models', 'iris', 'iris_fpv_cam.sdf')
    
    #custom_gazebo_models = os.path.join(blackdrones_description_dir, 'models')
    #px4_init = os.path.join(blackdrones_description_dir, 'PX4-init')

    os.makedirs(PX4_RUN_DIR, exist_ok=True)

    return LaunchDescription([
        SetEnvironmentVariable('GAZEBO_PLUGIN_PATH',
                               HOME + '/skyrats-workplace/src/PX4-Autopilot/build/px4_sitl_default/build_gazebo'),
        SetEnvironmentVariable('GAZEBO_MODEL_PATH', HOME + '/skyrats-workplace/src/PX4-Autopilot/Tools/sitl_gazebo/models'),

        SetEnvironmentVariable('PX4_SIM_MODEL', 'iris'),

        DeclareLaunchArgument('world', default_value=world),
        DeclareLaunchArgument('model', default_value=model),
        DeclareLaunchArgument('x', default_value='0.0'),
        DeclareLaunchArgument('y', default_value='0.0'),
        DeclareLaunchArgument('z', default_value='0.0'),
        DeclareLaunchArgument('R', default_value='0.0'),
        DeclareLaunchArgument('P', default_value='0.0'),
        DeclareLaunchArgument('Y', default_value='0.0'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([gazebo_launch_dir, '/gzserver.launch.py']),
            launch_arguments={'world': LaunchConfiguration('world'),
                              'verbose': 'true'}.items(),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([gazebo_launch_dir, '/gzclient.launch.py'])
        ),

        #ExecuteProcess(
        #    cmd=[
        #        'gz', 'model',
        #        '--spawn-file', LaunchConfiguration('model'),
        #        '--model-name', 'iris',
        #        '-x', LaunchConfiguration('x'),
        #        '-y', LaunchConfiguration('y'),
        #        '-z', LaunchConfiguration('z'),
        #        '-R', LaunchConfiguration('R'),
        #        '-P', LaunchConfiguration('P'),
        #        '-Y', LaunchConfiguration('Y')
        #    ],
        #    prefix="bash -c 'sleep 5s; $0 $@'",
        #    output='screen'),
        #
        #     
        #ExecuteProcess(
        #    cmd=[
        #        HOME + '/skyrats-workplace/src/PX4-Autopilot/build/px4_sitl_default/bin/px4',
        #        HOME + '/skyrats-workplace/src/PX4-Autopilot/ROMFS/px4fmu_common/',
        #        '-s',
        #        HOME + '/skyrats-workplace/src/PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/rcS'
        #    ],
        #    cwd=PX4_RUN_DIR,
        #    output='screen'),
])
