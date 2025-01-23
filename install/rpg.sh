#rpg ros
sudo apt-get install ros-noetic-camera-info-manager -y
sudo apt-get install ros-noetic-image-view -y
sudo apt-get install libcaer-dev -y
# sudo apt-get install python-catkin-tools -y

cd
mkdir -p rpg_ws/src
cd rpg_ws
# catkin config --init --mkdirs --extend /opt/ros/noetic --merge-devel --cmake-args -DCMAKE_BUILD_TYPE=Release

cd ~/rpg_ws/src
git clone https://github.com/catkin/catkin_simple.git

cd ~/rpg_ws/src
git clone https://github.com/uzh-rpg/rpg_dvs_ros.git
cd ..
catkin_make

