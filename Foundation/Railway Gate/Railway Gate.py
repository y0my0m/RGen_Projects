from machine import Pin, PWM
import time

pin_12 = Pin(12, Pin.OUT)
my_servo = PWM(pin_12, freq=50)

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def servo(pin, angle):
    pin.duty(map(angle, 0, 180, 20, 180))

for angle in range(0, 181, 1):  # Rotate from 0 to 180 degrees
    servo(my_servo, angle)
    time.sleep(0.02)  # Adjust speed of rotationfor angle in range(180, -1, -1):  # Rotate back from 180 to 0 degrees
    servo(my_servo, angle)
    time.sleep(0.02)  # Adjust speed of rotation    

