#!/usr/bin/env python
import rospy
from dotbot_msgs.msg import Led
import RPi.GPIO as GPIO


def led_cb(led):
    GPIO.output(7, led.led1)

def led_driver():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7,False)
    rospy.init_node('led_driver', anonymous=True)
    rospy.Subscriber("/dotbot/led", Led, led_cb)
    rospy.spin()

if __name__ == '__main__':
    led_driver()
