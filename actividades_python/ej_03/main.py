from gpiozero import LED, Buzzer
from time import sleep
from signal import pause

#declaro los pines de los leds y el buzzer
red = LED(19)
green = LED(13)
blue = LED(26)
buzz = Buzzer(22)

#variable de control de encendido de leds
x = 0
#declaro diccionario con instrucciones
dic = {"buzz on":0, "buzz off":1, "rgb red":3, "rgb blue":4, "rgb green": 5}

#función all
def all(act, x):
	print("inside")

	#LEDS.ON prende cada led según indique la entrada del prompt,
	#y deja constancia en la variable x de su encendido
	if(x == 0):
		if((dic[act]) == 3):
			x = 1
			red.on()
		elif((dic[act]) == 4):
			x = 2
			blue.on()
		elif((dic[act]) == 5):
			x = 3
			green.on()

		elif((dic[act]) == 0):
			buzz.on()
		elif((dic[act]) == 1):
			buzz.off()

	#LEDS.OFF apaga los leds si hubieran quedado encendidos
	else:
		if(x == 1):
			red.off()
		elif(x == 2):
			blue.off()
		elif(x == 3):
			green.off()

#bucle principal
while True:
	#solicito prompt
	act = input("prompt: ")

	#si hay un error de tipeo imprime error
	if(act not in dic):
		print("error")
	else:
		all(act, x)
