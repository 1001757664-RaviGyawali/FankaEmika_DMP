#!/usr/bin/env python
 
import rospy
import sys
import moveit_commander
from math import pi
 
class PickPlaceDemo:

    def __init__(self):

        rospy.init_node('pick_place', anonymous=True) 
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the move groups:
        self.arm = moveit_commander.MoveGroupCommander('panda_arm')  
        self.gripper = moveit_commander.MoveGroupCommander('panda_hand')

         # Set the Velocity and Acceleration limit:
        self.arm.set_max_velocity_scaling_factor(0.5)
        self.arm.set_max_acceleration_scaling_factor(0.25)

        self.gripper.set_max_velocity_scaling_factor(0.75)   
        self.gripper.set_max_acceleration_scaling_factor(0.5)

    def initial_pose(self):

        # Initial Standard Position for the Arm and the Gripper:
        rospy.loginfo("Going to Initial Pose of Arm and Hand.")
        arm_initial_pose = [0, -pi/4, 0, -3 * pi/4, 0, pi/2, pi/4]
        self.arm.set_joint_value_target(arm_initial_pose) 
        self.arm.go(wait=True)

        gripper_joint_positions = [0.0395, 0.0395] 
        self.gripper.set_joint_value_target(gripper_joint_positions)   
        #self.gripper.set_named_target("open") 
        self.gripper.go(wait=True)

    def pick(self):
       
        # Pick position
        rospy.loginfo("------------  Pick Position --------------.")
        pick_joint_angles = [0.7189732787624786, 0.2724582211244754, -0.2550385789745726, -2.60172525927895, -0.09904505834969411, 2.871021545622084, -1.1456585508882997] 
        self.arm.set_joint_value_target(pick_joint_angles)        
        self.arm.go(wait=True)

        rospy.loginfo("Gripper Closing.")
        gripper_joint_positions = [0.031827, 0.031827] #[0.0305, 0.0305]
        self.gripper.set_joint_value_target(gripper_joint_positions)
        #self.gripper.set_named_target("close")          
        self.gripper.go(wait=True)
    
    def intermediate_wp1(self):
        rospy.loginfo("------------  Intermediate Waypoint 1 --------------.")
        pick_joint_angles = [0.7164817005019439, -0.13362621335606822, -0.25310019651238547, -2.5209435518499004, -0.10986182010173798, 2.3992043515350976, -1.1456998863125012] 
        self.arm.set_joint_value_target(pick_joint_angles)      
        self.arm.go(wait=True)
    
    def intermediate_wp2(self):
        rospy.loginfo("------------  Intermediate Waypoint 2 --------------.")
        pick_joint_angles = [0.8153962626519956, 0.19132801606794522, -0.24823251548986242, -2.077540519647431, -0.014015307647486526, 2.3031918286217583, -1.1070045350838316]
        self.arm.set_joint_value_target(pick_joint_angles)     
        self.arm.go(wait=True)
 
    def place(self):
        rospy.loginfo("------------  Place Position --------------.")
        # Place position
        place_joint_angles = [0.80397496852331, 0.7929724769962138, -0.19297228469555838, -1.5040196179562841, 0.0830575788418452, 2.3078536557091605, -1.1081086419328219] 
        self.arm.set_joint_value_target(place_joint_angles)    
        self.arm.go(wait=True)

        rospy.loginfo("Gripper Opening.")
        gripper_joint_positions = [0.0395, 0.0395] 
        self.gripper.set_joint_value_target(gripper_joint_positions)
        #self.gripper.set_named_target("open")
        self.gripper.go(wait=True)
 
    def run(self):
        while not rospy.is_shutdown():
            self.pick()
            rospy.sleep(0.01)
            self.intermediate_wp1()
            rospy.sleep(0.01)
            self.intermediate_wp2()
            rospy.sleep(0.01)
            self.place()
            rospy.sleep(0.01)
            self.intermediate_wp2()
            rospy.sleep(0.01)
            self.intermediate_wp1()
            rospy.sleep(0.01)

if __name__ == '__main__':

    try:
        demo = PickPlaceDemo()
        demo.initial_pose()
        demo.run()

    except rospy.ROSInterruptException:
        pass

    finally:
        moveit_commander.roscpp_shutdown()