from gpiozero import LED, Button
from time import sleep
from signal import pause

led_r = LED(13)
led_v = LED(19)
led_a = LED(26)
button = Button(18)


button.when_pressed =led_r.on
##sleep(2)
button.when_released = led_r.off
sleep(1)
button.when_pressed = led_v.on
##sleep(2)
button.when_released = led_v.off()

button.when_pressed = led_a.on
##sleep(2)
button.when_released = led_a.off()

pause()
