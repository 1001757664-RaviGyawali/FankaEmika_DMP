# FrankaEmika_DMP

pyrdmp:

Serves as the library for the DMP framework


pick_place_pkg:

franka_kinesthetic_teaching.py -----> Records the joint_states while guiding the robot

SimpleExtractor.py -----> Converts a rosbag file into a '.txt' or a '.csv' file

trajectory_playback.py -----> Plays back the trajectory learned from the DMP framework

pick_place.py -----> Simple open-loop waypoint based pick and place demo



Note: All the other packages are the standard packages required to run the actual robot.



For Kinesthetic Teaching of the robot:

roslaunch franka_control franka_control.launch robot_ip:= xxxxxx 

rosrun pick_place_pkg franka_kinesthetic_teaching.py



For Trajectory Playback:

roslaunch franka_example_controllers trajectory_playback.launch robot_ip:= xxxxx

rosrun pick_place_pkg trajectory_playback.py
