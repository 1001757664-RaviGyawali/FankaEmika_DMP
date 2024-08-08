#!/usr/bin/env python

import sys
import rospy as ros
from actionlib import SimpleActionClient
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal, FollowJointTrajectoryResult

def load_trajectory_from_file(file_path):
    trajectory = []
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            values = [float(x) for x in line.strip().split(',')]
            time_from_start = values[0] * 1e-9  # Convert nanoseconds to seconds
            positions = values[1:]
            trajectory.append((time_from_start, positions))
    return trajectory

ros.init_node('move_to_start')

# Load trajectory from file
file_path = ros.get_param('~trajectory_file', '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/trajectory.txt')
trajectory = load_trajectory_from_file(file_path)

# Setup action client
action = ros.resolve_name('~follow_joint_trajectory')
client = SimpleActionClient(action, FollowJointTrajectoryAction)
ros.loginfo("move_to_start: Waiting for '{}' action to come up".format(action))
client.wait_for_server()
ros.loginfo("move_to_start: Action server up")

# Get joint names
topic = ros.resolve_name('~/joint_states')
ros.loginfo("move_to_start: Waiting for message on topic '{}'".format(topic))
joint_state = ros.wait_for_message(topic, JointState)
joint_names = joint_state.name

# Create and send trajectory goal
goal = FollowJointTrajectoryGoal()
for time_from_start, positions in trajectory:
    point = JointTrajectoryPoint()
    point.time_from_start = ros.Duration.from_sec(time_from_start)
    point.positions = positions
    point.velocities = [0] * len(positions)
    goal.trajectory.points.append(point)

goal.trajectory.joint_names = joint_names
goal.goal_time_tolerance = ros.Duration.from_sec(0.5)

ros.loginfo('Sending trajectory goal to execute the trajectory')
client.send_goal_and_wait(goal)

result = client.get_result()
if result.error_code != FollowJointTrajectoryResult.SUCCESSFUL:
    ros.logerr('move_to_start: Movement was not successful: ' + {
        FollowJointTrajectoryResult.INVALID_GOAL: "The joint pose you want to move to is invalid (e.g. unreachable, singularity...). Is the 'joint_pose' reachable?",
        FollowJointTrajectoryResult.INVALID_JOINTS: "The joint pose you specified is for different joints than the joint trajectory controller is claiming. Does you 'joint_pose' include all 7 joints of the robot?",
        FollowJointTrajectoryResult.PATH_TOLERANCE_VIOLATED: "During the motion the robot deviated from the planned path too much. Is something blocking the robot?",
        FollowJointTrajectoryResult.GOAL_TOLERANCE_VIOLATED: "After the motion the robot deviated from the desired goal pose too much. Probably the robot didn't reach the joint_pose properly"
    }[result.error_code])
else:
    ros.loginfo('move_to_start: Successfully executed the trajectory')
