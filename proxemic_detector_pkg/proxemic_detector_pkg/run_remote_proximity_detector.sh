cd ~/ros_class_ws/
source /opt/ros/galactic/setup.bash
colcon build
source install/setup.bash
colcon build --packages-select proxemic_detector_pkg
ros2 launch proxemic_detector_pkg proxemic_detector.launch.py
