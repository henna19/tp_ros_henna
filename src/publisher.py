#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from Tkinter import *
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped


def callback(data):

    pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)    
    rate = rospy.Rate(15) # 15hz
    message=PoseStamped()
    theta=0
    message.header.frame_id="map"
    print(message)

    if(data.data == True):
	while theta <= 2*(math.pi):
		message.pose.position.x=theta
		message.pose.position.y=math.sin(theta)
		pub.publish(message)
		rate.sleep()
	    	theta = theta + 0.1

	while theta >=0:
		message.pose.position.x=theta
		message.pose.position.y=math.sin(-theta)
		pub.publish(message)
		rate.sleep()
	    	theta = theta - 0.1
  
def listener():
    rospy.init_node('talker', anonymous=True)        
    rospy.Subscriber("button_state", Bool, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
