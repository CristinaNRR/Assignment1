#!/usr/bin/env python


import rospy

from beginner_tutorials.msg import Num
from std_msgs.msg import String
import time

#everytime the node control receive a via point just wait for a couple of seconds.
#later it sends back a feedbaack saying that the desired position has been reached
def callback(data):
    rospy.loginfo('go to via point: %s', data.num)
    time.sleep(4)

    pub = rospy.Publisher('flag', String, queue_size=15)
    string = 'goalReached'
    pub.publish(string)
    print(string)

def control():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('control', anonymous=True)
   # pub = rospy.Publisher('flag', String, queue_size=15)
    #string = 'READY!'
    #pub.publish(string)
    #print(string)

    rospy.Subscriber('viaPoint', Num, callback)



    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    control()
