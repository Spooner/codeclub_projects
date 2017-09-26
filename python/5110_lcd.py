from Adafruit_Nokia_LCD import PCD8544 as LCD, LCDWIDTH, LCDHEIGHT
import Adafruit_GPIO.SPI as SPI

from PIL import Image, ImageDraw, ImageFont

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Hardware SPI usage:
display = LCD(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
 
# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
 
# Initialize library.
display.begin(contrast=60)
 
# Clear display.
display.clear()
display.display()


# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCDWIDTH, LCDHEIGHT))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a white filled box to clear the image.
draw.rectangle((0, 0, LCDWIDTH, LCDHEIGHT), outline=255, fill=255)
 
# Draw some shapes.
draw.ellipse((2,2,22,22), outline=0, fill=255)
draw.rectangle((24,2,44,22), outline=0, fill=255)
draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
draw.line((68,22,81,2), fill=0)
draw.line((68,2,81,22), fill=0)
 
# Load default font.
font = ImageFont.load_default()
 
# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
 
# Write some text.
draw.text((8,30), 'Hello World!', font=font)
 
# Display image.
display.image(image)
display.display()
