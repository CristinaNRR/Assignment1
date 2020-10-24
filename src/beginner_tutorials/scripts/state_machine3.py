#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import String

import smach
import smach_ros
import time
import random
from beginner_tutorials.msg import Num

# INSTALLATION
# - create ROS package in your workspace:
#          $ catkin_create_pkg smach_tutorial std_msgs rospy
# - move this file to the 'smach_tutorial/scr' folder and give running permissions to it with
#          $ chmod +x state_machine.py
# - run the 'roscore' and then you can run the state machine with
#          $ rosrun smach_tutorial state_machine.py
# - install the visualiser using
#          $ sudo apt-get install ros-kinetic-smach-viewer
# - run the visualiser with
#          $ sudo apt-get install ros-kinetic-smach-viewer

def user_action(data):
    print(data)
    if(data=='PLAY'):
	return ('play')

    elif(data=='NORMAL'):
	return ('normal')

    else:
   	return random.choice(['sleep','normal'])
  



# define state Unlocked
class Normal(smach.State):
    def __init__(self):
        self.var='FALSE'
        rospy.Subscriber('chatter', Num, self.callback)
        # initialisation function, it should not wait
        smach.State.__init__(self, 
                             outcomes=['play','sleep', 'normal'])


    def execute(self,userdata):
	time.sleep(2)
        # function called when exiting from the node, it can be blacking
        print (self.var)
        rospy.loginfo('Executing state NORMAL ')
	if(self.var=='TRUE'):
		return user_action('PLAY')#i activate the play state
	else:
        
        	return user_action('RANDOM')

    def callback(self,data):
   
    	rospy.loginfo('I heard %s', data.num)
        if(data.num == (0,0,0,0,0,0)):
        	self.var = 'FALSE'
        else:
    		self.var = 'TRUE' #ask the normal state to activate the play state
        print(self.var)

    

# define state Locked
class Sleep(smach.State):
    def __init__(self):
        #self.var
        smach.State.__init__(self, 
                             outcomes=['play','sleep', 'normal'])
                          
       
        self.rate = rospy.Rate(200)  # Loop at 200 Hz

    def execute(self,userdata):
        time.sleep(2)
        # simulate that we have to get 5 data samples to compute the outcome
        while not rospy.is_shutdown():  
          
     
        	rospy.loginfo('Executing state SLEEP')
		
        
                return user_action('NORMAL')
               
            


# define state Locked
class Play(smach.State):
    def __init__(self):
	#self.var
        smach.State.__init__(self, 
                             outcomes=['play','sleep', 'normal'])
                          
       
        self.rate = rospy.Rate(200)  # Loop at 200 Hz

    def execute(self,userdata):
        time.sleep(2)
        # simulate that we have to get 5 data samples to compute the outcome
        while not rospy.is_shutdown():  

     	  
            rospy.loginfo('Executing state PLAY')
               
            return user_action('RANDOM')
           


class func():
  def __init__(self):
        
                       
    rospy.init_node('smach_example_state_machine') 

  
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['container_interface'])
   

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('NORMAL', Normal(), 
                               transitions={'normal':'NORMAL', 
                                            'play':'PLAY',
				             'sleep' : 'SLEEP'})
                                              
        smach.StateMachine.add('PLAY', Play(), 
                               transitions={'normal':'NORMAL', 
                                            'play':'PLAY',
				             'sleep' : 'SLEEP'})
	smach.StateMachine.add('SLEEP', Sleep(), 
                               transitions={'normal':'NORMAL', 
                                            'play':'PLAY',
				             'sleep' : 'SLEEP'})
                               
                               

    # Create and start the introspection server for visualization
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

 

if __name__ == '__main__':
    
    func()
