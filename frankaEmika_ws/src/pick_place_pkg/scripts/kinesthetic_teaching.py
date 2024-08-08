#!/usr/bin/env python

import sys
import rospy
import rosbag
import os
from sensor_msgs.msg import JointState
from franka_msgs.msg import FrankaState

class FrankaKinestheticTeaching():
    def __init__(self):
        self.bag = None
        self.recording = False
        self.bag_file_path = rospy.get_param('~bag_file_path','~/Desktop/KinestheticTeachingRecording/kinesthetic_teaching.bag')

        self.joint_states_subscriber = rospy.Subscriber('/joint_states', JointState, self.joint_state_cb)
        self.franka_states_subscriber = rospy.Subscriber('/franka_state_controller/franka_states', FrankaState, self.franka_state_cb)

        rospy.loginfo("Franka Kinesthetic Teaching is starting now ........... ")

    def joint_state_cb(self, msg):
        if self.recording and self.bag:
            self.bag.write('/joint_states', msg)
    
    def franka_state_cb(self, msg):
        if msg.robot_mode == 3 and not self.recording:
            rospy.loginfo("Guiding mode activated, starting recording .............")
            self.bag = rosbag.Bag(self.bag_file_path,'w')
            self.recording = True

        elif msg.robot_mode != 3 and self.recording:
            rospy.loginfo("Guiding mode disabled, stopping recording ..............")
            self.recording = False
            self.bag.close()

if __name__ == 'main':
    rospy.init_node('kinesthetic_teaching',anonymous=True)
    franka_kinesthetic_teaching = FrankaKinestheticTeaching()
    rospy.spin()
