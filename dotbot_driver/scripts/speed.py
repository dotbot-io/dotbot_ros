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
        self.stop_speed = 0

        self.pwm_sx = GPIO.PWM(sx[0], 50)
        self.pwm_dx = GPIO.PWM(dx[0], 50)

        self.pin_dx = dx[1]
        self.pin_sx = sx[1]
        rospy.init_node('speed_driver', anonymous=True)
        rospy.Subscriber("/dotbot/speed", Speed, self.on_speed)
        rate = rospy.Rate(1) # 10hz
        while not rospy.is_shutdown():
            self.stop_speed = self.stop_speed + 1
            if self.stop_speed > 2:
                GPIO.output(self.pin_sx, False)                
                GPIO.output(self.pin_sx, False)                
                self.pwm_sx.start(0)
                self.pwm_dx.start(0)
            rate.sleep()
            print(self.stop_speed)

    def on_speed(self, msg):
        self.stop_speed = 0
        if msg.sx < 0:
            GPIO.output(self.pin_sx, True)
            self.pwm_sx.start(msg.sx + 100)
        else:
            GPIO.output(self.pin_sx, False)
            self.pwm_sx.start(msg.sx)

        if msg.dx < 0:
            GPIO.output(self.pin_dx, True)
            self.pwm_dx.start(msg.dx + 100)
        else:
            GPIO.output(self.pin_dx, False)
            self.pwm_dx.start(msg.dx)

if __name__ == '__main__':
    n = SpeedNode()
