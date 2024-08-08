#!/usr/bin/env python
 
import rospy
import moveit_commander
import moveit_msgs.msg
from moveit_commander import PlanningSceneInterface, RobotCommander, MoveGroupCommander
import numpy as np
 
# Initialize the node
 
rospy.init_node('traj_execution1', anonymous=True)
 
# Initialize RobotCommander, PlanningSceneInterface, and MoveGroupCommander
 
robot = RobotCommander()
scene = PlanningSceneInterface()
group_name = "panda_arm"
move_group = MoveGroupCommander(group_name)
 
# Set the Velocity and Acceleration limit:
move_group.set_max_velocity_scaling_factor(0.01)
move_group.set_max_acceleration_scaling_factor(0.01)
 
# Load joint goals from a text file
file_path = '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/trajectory.txt'
data = np.loadtxt(file_path, delimiter=',', skiprows=1)
time_stamps = data[:,0]
joint_positions = data[:, 1:]
 
joint_goals = joint_positions.tolist()
time_stamps_list = time_stamps.tolist()
 
# Define a list of joint space goals
#joint_goals = [
#    [-8.787946047139816308e-01,2.648911158563017620e-01,6.580319886060312928e-01,-2.488217680484488437e+00,-2.319307249219209888e-01,2.636669191240874177e+00,1.424224399760929627e+00],
#    [-8.788288401719681620e-01,2.648643994441559069e-01,6.582129635641893461e-01,-2.488414913194097355e+00,-2.318881622366995299e-01,2.636672932999311492e+00,1.424227211742625121e+00],
#    [-8.788754518293260265e-01,2.648273332033989069e-01,6.585489879135817404e-01,-2.488760850858679152e+00,-2.318285483771921063e-01,2.636673974291743772e+00,1.424231171834828391e+00]
#]
 
# Function to plan a trajectory to a given joint goal
 
def plan_trajectory_to_joint_goal(joint_goal):
    move_group.set_joint_value_target(joint_goal)
    plan = move_group.plan()
 
    return plan
 
# Initialize an empty combined trajectory
 
combined_trajectory = moveit_msgs.msg.RobotTrajectory()
 
# Iterate through each joint goal and plan the trajectory
 
for i, joint_goal in enumerate(joint_goals):
    plan = plan_trajectory_to_joint_goal(joint_goal)
 
    if not plan.joint_trajectory.points:
        rospy.logerr("Planning failed for joint goal: %s", joint_goal)
        continue
    
    if not combined_trajectory.joint_trajectory.points:
        combined_trajectory.joint_trajectory = plan.joint_trajectory
        
        for j, point in enumerate(combined_trajectory.joint_trajectory.points):
            point.time_from_start = rospy.Duration(time_stamps_list[j])
    else:
        last_time = combined_trajectory.joint_trajectory.points[-1].time_from_start
        
        for j, point in enumerate(plan.joint_trajectory.points):
            combined_trajectory.joint_trajectory.points.append(point)
 
previous_time = rospy.Duration(0)
for point in combined_trajectory.joint_trajectory.points:
    if point.time_from_start <= previous_time:
        point.time_from_start = previous_time + rospy.Duration(0.01)
    previous_time = point.time_from_start
    
# Execute the combined trajectory
 
move_group.execute(combined_trajectory, wait=True)
 
# Keep the script running
 
rospy.spin()
 