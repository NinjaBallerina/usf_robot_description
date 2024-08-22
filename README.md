# USF Robot Description
This package provides a `ROS 2 Humble` setup for visualizing a 5 DOF 3D printed robot with a claw gripper in **RViz2**. Developed for the **University of South Florida**, this package allows users to interact with the robot using joint state publisher sliders.

## Features

- Visualize the 5 DOF robot model
- Interact with the robot using joint sliders
- URDF model with articulated claw gripper

## Prerequisites

- `ROS 2 Humble` installed
- `Colcon build` tool

## How to Use

1. ** Build the Package **
    colcon build

2. ** Source the ROS 2 Humble Environment **
    source /opt/ros/humble/setup.bash 

3. ** Source the Workspace **
    source install/setup.bash

4. ** Now, you are ready to launch the RViz2 Visualization **
    ros2 launch usf_robot_description display.launch.py

5. ** Interact with the Robot **
Use the joint state publisher sliders in **RViz2** to control and visualize the movement of the robot's joints, including the claw gripper.
