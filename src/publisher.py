#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from Tkinter import *
from std_msgs.msg import Bool
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped


class huit:
    def __init__(self):
	rospy.init_node('talker', anonymous=True)
	self.pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)    
	self.rate = rospy.Rate(15) # 15hz
	self.message=PoseStamped()
	self.theta=0
	self.state=None
	self.message.pose.position.x=self.theta
	self.message.pose.position.y=math.sin(self.theta)
	self.message.header.frame_id="map"

	rospy.Subscriber("button_state", Bool, self.callback)

    def callback(self,data):
	self.state = data.data

    def run(self):

	while not rospy.is_shutdown():
	    if(self.state == True):
		while (self.theta <= 2*(math.pi)):
			self.message.pose.position.x=(self.theta)
			self.message.pose.position.y=math.sin(self.theta)
			self.pub.publish(self.message)
			self.rate.sleep()
			self.theta = self.theta + 0.1
		while (self.theta >=0):
			self.message.pose.position.x=self.theta
			self.message.pose.position.y=math.sin(-self.theta)
			self.pub.publish(self.message)
			self.rate.sleep()
			self.theta = self.theta - 0.1
  

if __name__ == '__main__':
    try:
	node=huit()
	node.run()
    except rospy.ROSInterruptException:
	pass
