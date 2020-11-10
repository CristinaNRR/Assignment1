#!/usr/bin/env python


import rospy

from beginner_tutorials.msg import Num
from std_msgs.msg import String
import time

#everytime the node control receive a via point just wait for a couple of seconds.
#later it sends back a feedback saying that the desired position has been reached
def callback(data):
    rospy.loginfo('going to via point: %s', data.num)
    time.sleep(4)

    pub = rospy.Publisher('flag', String, queue_size=15)
    string = 'goalReached'
    pub.publish(string)
    print(string)

def control():

  
    rospy.init_node('control', anonymous=True)

    rospy.Subscriber('viaPoint', Num, callback)


    rospy.spin()

if __name__ == '__main__':
    control()
