from gpiozero import LED
from gpiozero import PWMLED
from time import sleep
import math
import ADS1x15

#Declaro pines de leds
led_rojo = PWMLED(19)
led_azul = PWMLED(26)

#Declaro valores propios de los componentes
vcc = 3.3
v_term = 0, r_term = 0, r1 = 10000
t = 0
x = 3977 # Factor de aumento del termistor

ADS = ADS1x15.ADS1115(1, 0x48)
ADS.setMode(ADS.MODE_SINGLE)
ADS.setGain(ADS.PGA_4_096V)

f = ADS.toVoltage()

while True :
	# Obtengo valores de presión y temperatura
	val_temperatura = ADS.readADC(1)
	val_presion = ADS.readADC(3)

	press = val_presion * f
	temp = val_temperatura * f

	# Cálculo de temperatura
	v_term = (vcc * temp) / 4095
	r_term = r1 / ((vcc / v_term) - 1)
	t = (x / math.log10 ((r_term / r1) + (x / 298))) - 273.15

	if (press > temp):
		led_red.value = (press - temp) * 0.2

		if (led_red.value > 1):
			led_red.value = 1
		time.sleep(1)
		
	elif (press < temp):
		led_blue.value = (temp - press) * 0.2
		
		if (led_blue.value > 1):
			led_blue.value = 1
		time.sleep(1)
		
	else:
		led_red.value = 0
		led_blue.value = 0
		time.sleep(1)
		
	# Imprimo los valores en consola
	print ("Valor de temperatura: {0:.3f} V".format(temp))
	print ("Valor de presión: {0:.3f} V".format(press))
	time.sleep(2)
