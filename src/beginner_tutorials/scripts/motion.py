#!/usr/bin/env python


import rospy
from std_msgs.msg import String

from beginner_tutorials.msg import Num


def callback(data):
    rospy.loginfo('received target position: %s', data.num)

    pub = rospy.Publisher('viaPoint', Num)
    msg= Num()
    msg.num= [0,0] 
    pub.publish(msg)
    

def callback2(data):

    rospy.loginfo('%s', data.data)
  
def motion():

 
    rospy.init_node('motion', anonymous=True)

    #listen for goalPositions coming from the state machine
    rospy.Subscriber('targetPosition', Num, callback)

    #the control node returns a flag when the target pose is reached
    rospy.Subscriber('flag', String, callback2)

   

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    motion()

 


