#!/usr/bin/env python
from gpiozero import LED
import rospy
from std_msgs.msg import UInt8

pub = rospy.Publisher('driver', UInt8, queue_size=10)
rospy.init_node('dotbot_driver')
r = rospy.Rate(1)
led = LED(21)
cnt = 0

while not rospy.is_shutdown():
   pub.publish(cnt)
   cnt = 1-cnt
   led.toggle()
   r.sleep()
