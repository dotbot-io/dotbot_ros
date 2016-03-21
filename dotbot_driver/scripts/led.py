#!/usr/bin/env python
import rospy
from dotbot_msgs.msg import Led
import RPi.GPIO as GPIO

led1 = 7
led2 = 8
led3 = 9

def led_cb(led):
    global led1
    global led2
    global led3
    GPIO.output(led1, led.led1)
    GPIO.output(led2, led.led2)
    GPIO.output(led3, led.led3)

def led_driver():
    global led1
    global led2
    global led3
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)
    GPIO.output(led1,False)
    GPIO.output(led2,False)
    GPIO.output(led3,False)
    rospy.init_node('led_driver', anonymous=True)
    rospy.Subscriber("/dotbot/led", Led, led_cb)
    rospy.spin()

if __name__ == '__main__':
    led_driver()
