#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#


import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Num
import random
import time

def perception():
    pub = rospy.Publisher('gesture', Num)
    rospy.init_node('perception', anonymous=True)
   
  
    while not rospy.is_shutdown():

		randomGesture = []
		for i in range(0,2):
			n = random.randint(1,10)
			randomGesture.append(n)
		pub.publish(randomGesture)
     		print(randomGesture)   
		
	
		time.sleep(15)
                


if __name__ == '__main__':
    try:
        perception()
    except rospy.ROSInterruptException:
        pass
