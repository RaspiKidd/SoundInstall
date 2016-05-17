import pygame.mixer
from pygame.mixer import Sound
from gpiozero import LED
from time import sleep

pygame.mixer.init ()

led = LED(17)
drum = Sound ("samples/drum_tom_mid_hard.wav")

while True:
	drum.play ()
	led.on ()
	sleep (0.05)
	led.off ()
	sleep (1)
