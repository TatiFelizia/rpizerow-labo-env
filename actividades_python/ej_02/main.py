from gpiozero import LED, Button
from time import sleep
from signal import pause

#declaro los distintos leds de acuerdo a sus colores
led_verde = LED(13)
led_rojo = LED(19)
led_azul = LED(26)

#bucle que enciende y apaga los leds
while True:
	led_rojo.on()
	sleep(1)
	led_rojo.off()
	#led rojo encendido durante 1 segundo, luego se apaga

	led_azul.on()
	sleep(0.5)
	led_azul.off()
	#led azul encendido, mantengo ese estado por medio segundo y apago

	led_verde.on()
	sleep(0.25)
	led_verde.off()
	#Led verde encendido por un cuarto de segundo y luego se apaga

pause()
