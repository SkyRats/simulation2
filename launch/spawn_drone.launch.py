import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir, LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    HOME = os.environ.get('HOME')
    PX4_RUN_DIR = HOME + '/tmp/px4_run_dir'
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=[
                                    '-file', LaunchConfiguration('sdf'),
                                    '-entity', LaunchConfiguration('model'), 
                                    '-x', LaunchConfiguration('x'),
                                    '-y', LaunchConfiguration('y'),
                                    '-z', LaunchConfiguration('z'),
                                    '-R', LaunchConfiguration('R'),
                                    '-P', LaunchConfiguration('P'),
                                    '-Y', LaunchConfiguration('Y')],
                                    output='screen')

    return LaunchDescription([
    SetEnvironmentVariable('PX4_SIM_MODEL', 'iris'),
    DeclareLaunchArgument('model', default_value='iris'),
    DeclareLaunchArgument('sdf', default_value='$(arg sdf)'),
    DeclareLaunchArgument('x', default_value='0.0'),
    DeclareLaunchArgument('y', default_value='0.0'),
    DeclareLaunchArgument('z', default_value='1.0'),
    DeclareLaunchArgument('R', default_value='0.0'),
    DeclareLaunchArgument('P', default_value='0.0'),
    DeclareLaunchArgument('Y', default_value='0.0'),
    spawn_entity,
    ExecuteProcess(
        cmd=[
            HOME + '/skyrats-workplace/src/PX4-Autopilot/build/px4_sitl_default/bin/px4',
            HOME + '/skyrats-workplace/src/PX4-Autopilot/ROMFS/px4fmu_common/',
            '-s',
            HOME + '/skyrats-workplace/src/PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/rcS'
        ],
        cwd=PX4_RUN_DIR,
        prefix="bash -c 'sleep 5s; $0 $@'",
        output='screen'),
    ])
