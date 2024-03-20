from gpiozero import LED, Button
from time import sleep
from signal import pause

#declaro pines
led = LED(26)
#led azul
button = Button(18)

#cuando el botón sea precionado, se va a prender el led
button.when_pressed = led.on
#cuando el botón se suelte, el led se apaga
button.when_released = led.off

#mantiene el programa corriendo
pause()
