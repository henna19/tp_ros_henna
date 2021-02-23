#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from geometry_msgs.msg import PoseStamped

def talker():
    pub = rospy.Publisher('published_topic', PoseStamped, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(15) # 10hz
    message=PoseStamped()
    print(message)
    message.pose.position.x=42
    print(message)
    while not rospy.is_shutdown():
        #theta=rospy.get_time()
        r=20
	theta=0
        message.header.frame_id="map"

	while theta < 2*(math.pi)
	    message.pose.position.x=theta
            message.pose.position.y=math.sin(theta)

	    pub.publish(message)
            rate.sleep()
    	    theta = theta + 0.1

        print(message)
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
