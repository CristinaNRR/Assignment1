#!/usr/bin/env python


import rospy
from std_msgs.msg import String

from beginner_tutorials.msg import Num

#when target position are received, the node sends a via point to the control node
def callback(data):
    rospy.loginfo('received target position: %s', data.num)

    pub = rospy.Publisher('viaPoint', Num)
    msg= Num()
    msg.num= [0,0] 
    pub.publish(msg)
    rospy.loginfo(msg)

def callback2(data):

    rospy.loginfo('%s', data.data)
  
def motion():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motion', anonymous=True)

    #listen for goalPositions coming from the state machine
    rospy.Subscriber('targetPosition', Num, callback)

    #control node return a flag when the target pose is reached
    rospy.Subscriber('flag', String, callback2)

   

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    motion()
