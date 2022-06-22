# Simulation2
Simulation2 is a ros2 package dedicated to simulating Micro Air Vehicles. It's developed and mainteined by students from Skyrats Autonomous Drone Team, from the University of São Paulo
## Prerequisites

- ROS2 with the PX4 firmware (developed on ROS Foxy) (recommended installaton: [skyrats-workplace](https://github.com/SkyRats/skyrats-workplace/tree/ros2))
- Suggestion: [mavbase2](https://github.com/SkyRats/mavbase2) ROS2 drone control package 

## How to use (user level)
The `scripts/` directory contains the two main files that need to be used in a user level. `simulate.sh` contains the specific details of every world we wish to simulate, giving the user the option to choose between them. `killgazebo.sh` is a simple script used to shutdown the simulation.

### Starting the desired simulation
Use `cd` to enter the `scripts/` directory of this package and run:
```bash
bash simulate.sh
```
Select the desired simulation by typing the matching number and pressing `enter`

### Shuting down a simulation
Use `Ctrl+C` on the terminal running the simulation and enter:
```bash
bash killgazebo.sh
```

## How to use (dev level)
To add a new simulation, edit the `simulate.sh` file in the `scripts/` directory. Copy and paste the indicated lines and change the parameters according to your necessity. Don't forget to edit the `INSERT_NUMBER_HERE` part and `echo` the new option indicating its number with the old ones.
