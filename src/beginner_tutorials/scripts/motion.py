#!/usr/bin/env python


import rospy

from beginner_tutorials.msg import Num

#everytime the node motion receive a position from the state machine it sends a null array to the node control.(It should send via points)
def callback(data):
    rospy.loginfo('I heard %s', data.num)

    pub = rospy.Publisher('viaPoint', Num)
    msg= Num()
    msg.num= [0,0] 
    pub.publish(msg)
    rospy.loginfo(msg)

def motion():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motion', anonymous=True)

    rospy.Subscriber('targetPosition', Num, callback)



    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    motion()
