from gpiozero import LED
from time import sleep

import time
import ADS1x15

#Declaro pin del led
led = LED(2)

ADS = ADS1x15.ADS1115(1, 0x48)

print("ADS1X15_LIB_VERSION: {}".format(ADS1x15.__version__))

# set gain to 4.096V max
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()

while True :
	print(f)
	val_1 = ADS.readADC(1)
	val_3 = ADS.readADC(3)
	print("Analog1: {0:d}\t{1:.3f} V".format(val_1, val_1 * f))
	print("Analog3: {0:d}\t{1:.3f} V".format(val_3, val_3 * f))
	time.sleep(2)
