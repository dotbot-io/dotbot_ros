#!/usr/bin/env python
import rospy
from dotbot_msgs.msg import Speed
import RPi.GPIO as GPIO


class InputNode():
    def __init__(self, bs = (3,5)):
        GPIO.setmode(GPIO.BOARD)
        for b in bs:
            GPIO.setup(dx[0], GPIO.IN)
        rate = rospy.Rate(1) # 10hz

        while not rospy.is_shutdown():
            for b in bs:
                print "input ", b, " : ", GPIO.input(b)


if __name__ == '__main__':
    n = InputNode()
