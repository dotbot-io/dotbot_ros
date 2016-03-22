#!/usr/bin/env python
import rospy
from dotbot_msgs.msg import Speed
import RPi.GPIO as GPIO


class SpeedNode():
    def __init__(self, dx = (15,16), sx = (21,22)):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(dx[0], GPIO.OUT)
        GPIO.setup(dx[1], GPIO.OUT)
        GPIO.setup(sx[0], GPIO.OUT)
        GPIO.setup(sx[1], GPIO.OUT)

        self.pwm_sx = GPIO.PWM(sx[0], 50)
        self.pwm_dx = GPIO.PWM(dx[0], 50)

        self.pin_dx = dx[1]
        self.pin_sx = sx[1]
        rospy.init_node('led_driver', anonymous=True)
        rospy.Subscriber("/dotbot/speed", Speed, self.on_speed)
        rospy.spin()

    def on_speed(self, msg):
        self.pwm_sx.start(msg.sx)
        self.pwm_dx.start(msg.dx)


def led_cb(led):
    GPIO.output(led1, led.led1)
    GPIO.output(led2, led.led2)
    GPIO.output(led3, led.led3)

def led_driver():
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
