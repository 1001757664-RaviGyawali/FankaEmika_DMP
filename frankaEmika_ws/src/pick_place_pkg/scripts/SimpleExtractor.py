#!/usr/bin/env python

#import sys
#sys.path.insert(0,'/home/developer/frankaEmika_ws/src/pyrdmp/pyrdmp')
#export PYTHONPATH=/home/developer/frankaEmika_ws/src/pyrdmp:$PYTHONPATH
import rosbag
import pandas as pd

bag_file = '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/KinestheticTeaching_multiplegoals.bag'
output_file_CSV = '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/KinestheticTeaching_multiplegoals.csv'
output_file_TXT = '/home/developer/frankaEmika_ws/src/pyrdmp/examples/data/KinestheticTeaching_multiplegoals.txt'

joint_names = ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7', 'panda_finger_joint1', 'panda_finger_joint2']    
bag = rosbag.Bag(bag_file)
data = []

for topic, msg, t in bag.read_messages(topics=['/joint_states']):
    time = t.to_sec()
    positions = {}
    
    for i, name in enumerate(msg.name):
        positions[name] = msg.position[i] 
        
    positions['time'] = time
    data.append(positions)

columns = ['time'] + joint_names
dataFrame = pd.DataFrame.from_records(data, columns=columns)
dataFrame.sort_values('time', inplace=True)
dataFrame.to_csv(output_file_TXT, index=False)
bag.close()