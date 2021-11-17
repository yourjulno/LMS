import bloodFunctions as b
import RPi.GPIO as GPIO
import spidev 
import numpy as np
import time
import matplotlib.pyplot as plt


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1600000
print ("SPI for ADC have been initialized")

def getAdc():
    adcResponse = spi.xfer2([0, 0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1

try:
    measure = []
    st0 = time.time()
    st = time.time()
    while st - st0 < 60: #здесь достаточно поменять одну цифру, чтобы изменить время, в течение которого измерялось давление
        st = time.time()
        measure.append(getAdc())

    b.save(measure, st0, st)
    measure = map(str, measure)

   
    plt.plot(measure)
    plt.show()

finally:
    spi.close()