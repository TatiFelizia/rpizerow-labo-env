from gpiozero import LED
from gpiozero import PWMLED
import time
import math
import ADS1x15

#Declaro pines de leds
led_red = PWMLED(19)
led_blue = PWMLED(26)

#Declaro valores propios de los componentes
vcc = 3.3
r1 = 10000
x = 3977 # Factor de aumento del termistor

#Configuro el adc
ADS = ADS1x15.ADS1115(1, 0x48)
ADS.setMode(ADS.MODE_SINGLE)
ADS.setGain(ADS.PGA_4_096V)

#Factor de conversión del adc
f = ADS.toVoltage()

while True :
	# Obtengo valores de presión y temperatura leídos por el adc
	val_temperatura = ADS.readADC(1)
	val_presion = ADS.readADC(3)

	# Multiplico por el factor de conversión del adc obteniendo la tensión de cada uno
	press = val_presion * f
	temp = val_temperatura * f

	# Cálculo de temperatura
	v_term = (vcc * temp) / 4095
	r_term = r1 / ((vcc / v_term) - 1)
	t = (x / math.log10((r_term / r1) + (x / 298.0))) - 273.15

	#Condiciones relacionadas al encendido de los leds
	#Si la presión es mayor a la temperatura, el led que prevalecerá encendido será el rojo
	if (press > temp):
		led_red.value = (press - temp) * 0.2

		if (led_red.value > 1):
			led_red.value = 1
		time.sleep(1)

	#Si la presión es menor a la temperatura el led que prevalece es el azul
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
	print ("V de temperatura: {0:.3f} V\n".format(temp))
	print ("Valor de temperatura: {0:.3f} T\n".format(t))
	print ("V de presión: {0:.3f} V\n\n".format(press))
	time.sleep(2)
