#!/usr/bin/env python

import rospy
import sys
import moveit_commander
 
def list_move_groups():
	# Initialize the node
    rospy.init_node('list_move_groups', anonymous=True)
 
    # Initialize MoveIt Commander
    moveit_commander.roscpp_initialize(sys.argv)
 
    # Initialize RobotCommander
    robot = moveit_commander.RobotCommander()
 
    # Get the names of all the planning groups
    group_names = robot.get_group_names()
 
    rospy.loginfo("Available Planning Groups:")
    for name in group_names:
        rospy.loginfo(name)
 
    # Shutdown MoveIt Commander
    moveit_commander.roscpp_shutdown()
 
if __name__ == '__main__':
	try:
		list_move_groups()
	except rospy.ROSInterruptException:
		pass
