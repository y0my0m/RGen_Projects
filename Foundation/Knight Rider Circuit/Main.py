import time
from machine import Pin

# Define the LED pins
led_pins = [Pin(1,Pin.OUT),Pin(2,Pin.OUT),Pin(3,Pin.OUT),Pin(4,Pin.OUT),Pin(5,Pin.OUT)] # Modify the pin numbers based on your board
# Function to create the Knight Rider effect
def knight_rider_effect():
   
while True:
        # Move left to right
        for i in range(len(led_pins)):
            led_pins[i].on()
            time.sleep(0.1)
            led_pins[i].off()
        
        # Move right to left
        for i in range(len(led_pins)-1, -1, -1):
            led_pins[i].on()
            time.sleep(0.1)
            led_pins[i].off()

# Run the Knight Rider effect
knight_rider_effect()


led_pins=[Pin.OUT(1)]