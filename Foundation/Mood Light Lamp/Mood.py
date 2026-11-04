from machine import Pin,PWM
from time import sleep

redp=Pin(12,Pin.OUT)
greenp=Pin(13,Pin.OUT)
bluep=Pin(14,Pin.OUT)

red=PWM(redp,freq=50)
green=PWM(greenp,freq=50)
blue=PWM(bluep,freq=50)

def map_value(x,in_min, in_max, out_min, out_max):
    return int((x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min)

def Light(redval,greenval,blueval):
    red.duty(map_value(redval,0,255,1023,0))
    green.duty(map_value(greenval,0,255,1023,0))
    blue.duty(map_value(blueval,0,255,1023,0))

def color_change(color):
    if color=='magenta':
      Light(255, 0, 255)
    elif color=='orange':
        Light(255, 165, 0)
    elif color=='purple':
        Light(128, 0, 128)
    elif color=='white':
        Light(255, 255, 255)
    elif color=='brown':
        Light(150, 75, 0)
    elif color=='gray':
        Light(128, 128, 128)
    elif color=='teal':
        Light(0, 128, 128)
    elif color=='nawy':
        Light(0, 0, 128)

while True:   
    color_change('magenta')
    sleep(1)
    color_change('orange')
    sleep(1)
    color_change('purple')
    sleep(1)
    color_change('white')
    sleep(1)
    color_change('brown')
    sleep(1)
    color_change('gray')
    sleep(1)
    color_change('teal')
    sleep(1)
    color_change('nawy')
    sleep(1)