SIMULATION_DIR="$HOME/skyrats-workplace/src/PX4-Autopilot"
FIRMWARE_DIR="$HOME/skyrats-workplace/src/PX4-Autopilot"
FIRMWARE_BUILD_DIR="$HOME/skyrats-workplace/src/PX4-Autopilot/build/px4_sitl_default"
source /usr/share/gazebo/setup.sh
# Types of drones
#declare -a TYPES_OF_DRONES
#TYPES_OF_DRONES="ropped_iris ropped_swarm iris iris_depth_camera iris_downward_depth_camera iris_fpv_cam iris_rplidar iris_stereo_camera"

cd $FIRMWARE_DIR 

# Setup Gazebo to find PX4
source Tools/setup_gazebo.bash $FIRMWARE_DIR $FIRMWARE_BUILD_DIR

# Setup ROS to find the PX4 packages
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$FIRMWARE_DIR
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$FIRMWARE_DIR/Tools/sitl_gazebo

# Setup Gazebo to find this package's models and plugins
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:${SIMULATION_DIR}/models
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:${SIMULATION_DIR}/build/px4_sitl_default/build_gazebo

# Setup skyrats interface for gazebo
 > ~/.gazebo/gui.ini
echo -e "[geometry]\nx=0\ny=0\n[overlay_plugins]\nfilenames=libskyrats_interface.so" >> ~/.gazebo/gui.ini


#cd $HOME/skyrats-workplace/src/PX4-Autopilot/Tools/sitl_gazebo/worlds
#gazebo aruco.world --verbose


cd $HOME/skyrats-workplace/src/PX4-Autopilot
make px4_sitl gazebo_iris_fpv_cam


##future ideas##

#SIM SPEED CONTROL
##export PX4_SIM_SPEED_FACTOR=2

#Different models and worlds
##make px4_sitl gazebo_iris_irlock__sonoma_raceway

#Verbose mode
##export VERBOSE_SIM=1
