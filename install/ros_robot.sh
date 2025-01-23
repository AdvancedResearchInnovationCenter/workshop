sudo apt install python-is-python3 python3-pip -y
pip install scipy
pip install --user ur_rtde
cd ~/rpg_ws/src
git clone -b py3 https://github.com/AdvancedResearchInnovationCenter/ros_robot
cd ~/rpg_ws
catkin_make