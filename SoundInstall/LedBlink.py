from gpiozero import LED
from time import sleep

led1 = LED( 18)
led2 = LED (25)
led3 = LED (12)
led4 = LED (17)
led5 = LED (21)

while True:
	led1.on ()
	sleep (0.1)
	led1.off ()
	sleep (0.5)
	
	led2.on ()
	sleep (0.1)
	led2.off ()
	sleep (0.5)
	
	led3.on ()
	sleep (0.1)
	led3.off ()
	sleep (0.5)

	led4.on ()
	sleep (0.1)
	led4.off ()
	sleep (0.5)

	led5.on ()
	sleep (0.1)
	led5.off ()
	sleep (0.5)

	
