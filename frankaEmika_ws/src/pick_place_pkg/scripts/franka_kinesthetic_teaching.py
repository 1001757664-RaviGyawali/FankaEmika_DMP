#!/usr/bin/env python

# -----------------     Joint State Recorder --Kinesthetic Teaching of Franka Emika Arm ------------- #
# Ravi Gyawali

import rospy
import rosbag
from sensor_msgs.msg import JointState
from franka_msgs.msg import FrankaState
from datetime import datetime


class FrankaKinestheticTeaching:

    def __init__(self):

        rospy.init_node('franka_kinesthetic_teaching',anonymous=True)
        
        self.bag = None
        self.recording = False
        self.bag_file_path = '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/KinestheticTeaching' 

        self.joint_states_subscriber = rospy.Subscriber('/joint_states', JointState, self.joint_state_cb)
        self.franka_states_subscriber = rospy.Subscriber('/franka_state_controller/franka_states', FrankaState, self.franka_state_cb)

        rospy.loginfo("............. Start Franka Kinesthetic Teaching now ........... ")

    def joint_state_cb(self, msg):
        
        if self.recording == True and self.bag != None:
            self.bag.write('/joint_states', msg)
            rospy.loginfo("................ Kinesthetic Teaching in progress .............")
    
    def franka_state_cb(self, msg):
        
        if msg.robot_mode == 3 and self.recording == False:
            rospy.loginfo(".......... Guiding mode activated, recording joint states .............")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            bag_filename = self.bag_file_path + "_" + timestamp + ".bag"
            self.bag = rosbag.Bag(bag_filename,'w')
            self.recording = True

        elif msg.robot_mode != 3 and self.recording == True:
            rospy.loginfo(".............. Guiding mode disabled, recording stopped ..............")
            self.recording = False
            self.bag.close()

if __name__ == '__main__':
    
    try: 
        franka_kinesthetic_teaching = FrankaKinestheticTeaching()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
