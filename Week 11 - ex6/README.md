# Read GPS and Plan Path

In order to use the gps reader scripts, you need ROS and Mavlink Lora set up.

Steps for that:
- install [ROS Melodic](https://wiki.ros.org/melodic/Installation/Ubuntu)
- set up your [catkin workspace](https://wiki.ros.org/catkin/Tutorials/create_a_workspace)
- copy the Mavlink Lora files from lecture files so that your structure looks like ```<catkin_workspace/src/mavlink_lora/CMakeLists.txt>```
- add ```source devel/setup.bash``` to your bash.rc
- run a ros node with ```roslaunch mavlink_lora mavlink_lora.launch serial_device:=/dev/ttyUSB0 serial_baudrate:=57600 heartbeats:=true``` to connect with a radio
- run ros with ```roslaunch mavlink_lora mavlink_lora.launch serial_device:=/dev/ttyACM0 serial_baudrate:=115200 heartbeats:=true``` to connect to flight controller directly with USB