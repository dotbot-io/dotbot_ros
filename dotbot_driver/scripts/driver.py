#!/usr/bin/env python
import rospy
from dotbot_msgs.msg import Speed, Led, Input
import RPi.GPIO as GPIO

class DriverNode():

    def __init__(self, dx = (15,16), sx = (21,22)):
        GPIO.setmode(GPIO.BOARD)
        rospy.init_node('driver')
        self.init_inputs()
        self.init_leds()
        self.init_speed()
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            self.check_reset_speed()
            self.pub_inputs()
            rate.sleep()

    def init_speed(self, dx = (15,16), sx = (21,22)):
        GPIO.setup(dx[0], GPIO.OUT)
        GPIO.setup(dx[1], GPIO.OUT)
        GPIO.setup(sx[0], GPIO.OUT)
        GPIO.setup(sx[1], GPIO.OUT)
        GPIO.setup(dx[0], GPIO.OUT)
        GPIO.setup(dx[1], GPIO.OUT)
        #self.pwm_sx = GPIO.PWM(sx[0], 100)
        #self.pwm_dx = GPIO.PWM(dx[0], 100)

        self.pin_dx = dx
        self.pin_sx = sx
        rospy.Subscriber("speed", Speed, self.on_speed)

        self.stop_speed = 0

    def check_reset_speed(self):
        self.stop_speed += 1
        if self.stop_speed > 20:
            GPIO.output(self.pin_dx[0], False)
            GPIO.output(self.pin_sx[0], False)
            GPIO.output(self.pin_dx[1], False)
            GPIO.output(self.pin_sx[1], False)

    def init_leds(self, leds = (7,11,12)):
        self.leds = leds
        GPIO.setup(self.leds[0], GPIO.OUT)
        GPIO.setup(self.leds[1], GPIO.OUT)
        GPIO.setup(self.leds[2], GPIO.OUT)
        GPIO.output(self.leds[0],False)
        GPIO.output(self.leds[1],False)
        GPIO.output(self.leds[2],False)
        rospy.Subscriber("led", Led, self.on_led)

    def init_inputs(self, inputs=(3,5)):
        self.inputs = inputs
        GPIO.setup(self.inputs[0], GPIO.IN)
        GPIO.setup(self.inputs[1], GPIO.IN)
        self.pub_input = rospy.Publisher('input', Input, queue_size=10)

    def pub_inputs(self):
        msg = Input()
        msg.input1 = GPIO.input(self.inputs[0])
        msg.input2 = GPIO.input(self.inputs[1])
        self.pub_input.publish(msg)

    def on_speed(self, msg):
        self.stop_speed = 0
        if msg.sx < 0:
            GPIO.output(self.pin_sx[0], True)
            GPIO.output(self.pin_sx[1], False)
        else:
            GPIO.output(self.pin_sx[1], True)
            GPIO.output(self.pin_sx[0], False)

        if msg.dx < 0:
            GPIO.output(self.pin_dx[0], True)
            GPIO.output(self.pin_dx[1], False)
        else:
            GPIO.output(self.pin_dx[1], True)
            GPIO.output(self.pin_dx[0], False)

    def on_led(self, led):
        GPIO.output(self.leds[0], led.led1)
        GPIO.output(self.leds[1], led.led2)
        GPIO.output(self.leds[2], led.led3)


if __name__ == '__main__':
    try:
        n = DriverNode()
    finally:
        GPIO.cleanup()
