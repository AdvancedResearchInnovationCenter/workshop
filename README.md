# ARIC Neuromorphic workshop
Slides found on sharepoint https://kuacae.sharepoint.com/:f:/s/IntelligentRoboticManufacturing/EhhggcLJJK1BhDGhZAAR8lIB4ZKO50gHpBKAYa8qvod22Q?e=741ZVE 
## Software

Prerequsites
1. Ubuntu 20.04

In the `install/` directory you will find scripts to install all the software you will need for this workshop. 
1. `install/ros.sh` will install ros noetic
2. `install/rpg.sh` will install the required ROS drivers for the cameras we will be using (built without catkin_simple)
3. `install/ros_robot.sh` will install ros_robot package
4. run `pip install -r requirements.txt` to install python dependencies

This tutorial will work the the system's default python installtion. For advanced use later on, you can pick and choose your python environment accordingly by adjusting the scripts above.

For day1 continue with `day1/day1_ws.ipynb`.

The above installtion will create a catkin workspace in your home directory called `rpg_ws`. 
