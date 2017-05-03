#!/usr/bin/env python
import rospy
from dotbot_msgs.msg import Input
import RPi.GPIO as GPIO


class InputNode():
    def __init__(self, bs = (3,5)):
        pub = rospy.Publisher('input', Input, queue_size=10)
        rospy.init_node('input_driver', anonymous=True)
        GPIO.setmode(GPIO.BOARD)
        for b in bs:
            GPIO.setup(b, GPIO.IN)
        rate = rospy.Rate(5) # 10hz

        while not rospy.is_shutdown():
            msg = Input()
            msg.input1 = GPIO.input(bs[0])
            msg.input2 = GPIO.input(bs[1])
            pub.publish(msg)
            rate.sleep()


if __name__ == '__main__':
    n = InputNode()
