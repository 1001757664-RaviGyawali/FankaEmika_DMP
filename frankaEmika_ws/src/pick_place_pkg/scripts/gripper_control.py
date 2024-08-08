#!/usr/bin/env python
 
import rospy

import sys

import moveit_commander

from sensor_msgs.msg import JointState
 
class GripperControl:

    def __init__(self):

        rospy.init_node('gripper_control', anonymous=True)  # Initialize the node
 
        moveit_commander.roscpp_initialize(sys.argv) # Initialize MoveIt Commander
 
        robot = moveit_commander.RobotCommander() # Initialize the move group for the gripper
        group_names = robot.get_group_names()
        print "============ Available Planning Groups:", robot.get_group_names()

        self.gripper = moveit_commander.MoveGroupCommander('panda_hand')
    
    def set_gripper(self, width, speed):
		joint_state = JointState()
		joint_state.name = ['panda_finger_joint1','panda_finger_joint2']
		joint_state.position = [width, width]
		joint_state.velocity = [speed, speed]
		
		self.gripper.set_joint_value_target(joint_state)
		
		self.gripper.go(wait=True)
 
    def open_gripper(self):

        # Open the gripper

        # self.gripper.set_named_target('open')

        # self.gripper.go(wait=True)

        rospy.loginfo("Gripper Opening.")
        
        self.set_gripper(0.040,0.05)
 
    def close_gripper(self):

        # Close the gripper

        # self.gripper.set_named_target('close')

        # self.gripper.go(wait=True)

        rospy.loginfo("Gripper Closing.")
        
        self.set_gripper(0.020, 0.05)
        
 
if __name__ == '__main__':

    try:

        gripper_control = GripperControl()

        gripper_control.open_gripper()

        rospy.sleep(1)

        gripper_control.close_gripper()
        
        rospy.sleep(1)
        
        gripper_control.open_gripper()
        
        rospy.sleep(1)
        
        gripper_control.close_gripper()
        

    except rospy.ROSInterruptException:

        pass

    finally:

        moveit_commander.roscpp_shutdown()
