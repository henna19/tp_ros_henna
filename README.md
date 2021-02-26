# tp_ros_henna
This package contains a node publisher.py that will calculate the coordiantes of x and y in order to follow the trajectory of an infinte loop. The package also contains a launch file which will automatically open the rviz software along with a toggle button. The button will have the functionality of controlling the motion.


##To install this package 
First install the toggle button package at : https://github.com/Kramoth/button_gui.git

Clone it into the src folder in your catkin workspace 

```sh
cd ~/catkin_ws/src
git clone https://github.com/Kramoth/button_gui.git
catkin build
source ~/catkin_ws/devel/setup.bash
```

Then repeat the same process with this package:

```sh
cd ~/catkin_ws/src
git clone https://github.com/henna19/tp_ros_henna.git
catkin build
source ~/catkin_ws/devel/setup.bash
```

##To run this node
After following the installation process, run the follwing code in the catkin workspace

```sh
roslaunch tp_ros_henna pub.launch
```

