#!/usr/bin/env python
 
import rospy
import sys
import moveit_commander
import numpy as np
from math import pi
 
class trajectoryExecution:

    def __init__(self):

        rospy.init_node('traj_execution', anonymous=True) 
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the move groups:
        self.arm = moveit_commander.MoveGroupCommander('panda_arm')  
        
        # Set the Velocity and Acceleration limit:
        self.arm.set_max_velocity_scaling_factor(0.25)
        self.arm.set_max_acceleration_scaling_factor(0.25)

    def initial_pose(self):

        # Initial Standard Position for the Arm and the Gripper:
        rospy.loginfo("Going to Initial Pose of Arm.")
        arm_initial_pose = [0, -pi/4, 0, -3 * pi/4, 0, pi/2, pi/4]
        self.arm.set_joint_value_target(arm_initial_pose) 
        self.arm.go(wait=True)
 
    def load_trajectory(self, file_path):
        rospy.loginfo("Loading the trajectory.")
        data = np.loadtxt(file_path, delimiter=',', skiprows=1)
        self.joint_positions = data[:, 1:]
 
    def execute_trajectory(self):
        rospy.loginfo("Trajectory began")
        for i in range(len(self.joint_positions)):
 
            self.arm.set_joint_value_target(self.joint_positions[i])
            self.arm.go(wait=True)
            #rospy.sleep(0.000001)
            rospy.loginfo("Trajectory is executing")
            
        rospy.loginfo("Trajectory executed")  
    def run(self):

        file_path = '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/trajectory.txt'
        self.load_trajectory(file_path)
        self.execute_trajectory()
 
if __name__ == '__main__':

    try:

        traj_exec = trajectoryExecution()
        traj_exec.initial_pose()
        traj_exec.run()

    except rospy.ROSInterruptException:

        pass

    finally:

        moveit_commander.roscpp_shutdown()
