#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ws2801example import  wheel
import time
import RPi.GPIO as GPIO
import threading
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 51
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)
 


def rainbow_cycle_successive(pixels, wait=0.1):

	t = threading.currentThread()
	
	for i in range(pixels.count()):
	    # tricky math! we use each pixel as a fraction of the full 96-color wheel
	    # (thats the i / strip.numPixels() part)
	    # Then add in j which makes the colors go around per pixel
	    # the % 96 is to make the wheel cycle around
	    pixels.set_pixel(i, wheel(((i * 256 // pixels.count())) % 256) )
	    pixels.show()
	    pixels.clear()
	    print(str(i))
	    if getattr(t,"do_run", False):
	    	pixels.clear()
	    	print("stopped by if getattr")
	    	break
	    else:
	    	print ("do_run is on")
	    	print(getattr(t,"do_run"))
	    if wait > 0:
	        time.sleep(wait)
	pixels.clear()
	print("stopped by getattr")
	print(getattr(t,"do_run"))
#while 1:

t = threading.Thread(target=rainbow_cycle_successive,args=(pixels,0.2,))
t.do_run = True
t.start()

time.sleep(2)
print("waited 2")
t.do_run = False
print("do_run off")
t.join()
pixels.clear()
pixels.show() 
