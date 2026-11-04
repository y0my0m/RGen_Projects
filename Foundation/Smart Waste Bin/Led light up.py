from machine import Pin
import time

# Initialize the LED pin
led = Pin(2, Pin.OUT)
#Adding Buzzer Variable
buzzer=Pin(15,Pin.OUT)

def buzzer_buzzing():
    while True:
        buzzer.value(1) #buzzer buzzes
        time.sleep(2) #waits 2 seconds
        buzzer.value(0) #buzzer stops buzzing
        time.sleep(2) #waits 2 seconds

# Function to turn on the LED
def light_up_bin():
    led.on()# Turn on LED
    time.sleep(10)# Keep the LED on for 10 seconds

light_up_bin()
buzzer_buzzing()
        