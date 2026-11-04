from machine import Pin, I2C
import ssd1306
import framebuf
import time

# ESP32 Pin assignment
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# Initialize the LED pin
led = Pin(2, Pin.OUT)
#Adding Buzzer Variable
buzzer=Pin(15,Pin.OUT)

oled_width = 128
oled_height= 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#buzzer part
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

def draw_large_text(display, text, x, y, scale=2):
    # Uses the base 8x8 font but draws it pixel by pixel at a larger scale
    
    # Create a temporary buffer to capture the standard font pixels
    # This buffer only needs to be large enough for one character (8x8)
    temp_buffer = bytearray(8 * 8 // 8) # 8 bytes for 8x8 monochrome
    temp_fbuf = framebuf.FrameBuffer(temp_buffer, 8, 8, framebuf.MONO_HLSB)
    
    for char_index, char in enumerate(text):
        # 1. Draw the single 8x8 character onto the temporary buffer
        temp_fbuf.fill(0) # Clear temp buffer
        temp_fbuf.text(char, 0, 0, 1) # Draw character 'char' at (0,0) in temp
        
        # 2. Read pixels from the temp buffer and scale them to the main display
        for px in range(8):
            for py in range(8):
                if temp_fbuf.pixel(px, py):
                    # If the pixel is set in the 8x8 font, draw a 'scale' x 'scale' block
                    for sx in range(scale):
                        for sy in range(scale):
                            display.pixel(x + (char_index * 8 * scale) + (px * scale) + sx, 
                                          y + (py * scale) + sy, 
                                          1)

# Clear the screen buffer
oled.fill(0)

# Use the new function instead of oled.text()
# Scale=2 makes text 16x16 pixels
draw_large_text(oled, "Reduce", 0, 0, scale=2)
draw_large_text(oled, "Reuse", 0, 18, scale=2) 
draw_large_text(oled, "Recycle", 0, 36, scale=2)

# Display the buffer content
oled.show()
light_up_bin()
buzzer_buzzing()
