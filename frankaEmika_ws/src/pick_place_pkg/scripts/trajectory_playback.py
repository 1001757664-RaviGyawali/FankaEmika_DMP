#!/usr/bin/env python

import rospy as ros
from actionlib import SimpleActionClient
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal, FollowJointTrajectoryResult

# Initialize ROS node
ros.init_node('trajectory_playback')

# Set up action client
action = '/effort_joint_trajectory_controller/follow_joint_trajectory'
client = SimpleActionClient(action, FollowJointTrajectoryAction)
ros.loginfo("Waiting for '" + action + "' action to come up")
client.wait_for_server()

# Read the file
file_path = '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/DMP_KinestheticTeaching_multiplegoals.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extract headers (joint names)
headers = lines[0].strip().split(',')
joint_names = headers[1:]
print("Joint names: {}".format(joint_names))

# Create a goal
goal = FollowJointTrajectoryGoal()
goal.trajectory.joint_names = joint_names

# Creating Time vector:
time_vec = []
k = 0.5

for i in range(555):
	time_vec.append(k)
	k+= 0.025

for index, line in enumerate(lines[1:]):
    values = line.strip().split(',')
    time = time_vec[index] 
    positions = [float(pos) for pos in values[1:]]
    point = JointTrajectoryPoint()
    point.positions = positions
    point.time_from_start = ros.Duration(time)
    goal.trajectory.points.append(point)

# Send goal and wait for result
ros.loginfo('Sending goal...')
client.send_goal_and_wait(goal)
ros.loginfo('Goal sent, waiting for result...')

# Get result
result = client.get_result()

if result is None:
    ros.logerr('No result received from action server. The goal might have been rejected or the server is not available.')
else:
    if result.error_code != FollowJointTrajectoryResult.SUCCESSFUL:
        ros.logerr("Movement was not successful. Error code: {}".format(result.error_code))
    else:
        ros.loginfo("Successfully moved through waypoints.")
