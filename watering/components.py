import RPi.GPIO as GPIO
import time

class pump:
    def __init__(self, control_pin=4):

        self.control_pin = control_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.control_pin, GPIO.OUT)

    def off(self):
        GPIO.output(self.control_pin, GPIO.LOW)

    def on(self, seconds=None):
        GPIO.output(self.control_pin, GPIO.HIGH)
        if seconds is not None:
            time.sleep(seconds)
            self.off()
