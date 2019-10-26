from ws2801example import rainbow_cycle, rainbow_cycle_successive
import time
import RPi.GPIO as GPIO
from threading import Thread 
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 50
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)
 


#while 1:

Thread(target=rainbow_cycle_successive,args=(pixels,0.2 )).start()
print ("finished cycle")
pixels.show()
pixels.clear()
pixels.show() 
