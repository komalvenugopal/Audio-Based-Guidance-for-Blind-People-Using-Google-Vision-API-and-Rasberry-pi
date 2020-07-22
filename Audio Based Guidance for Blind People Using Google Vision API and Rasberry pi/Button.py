#python3 -m pip install RPi.GPIO

import RPi.GPIO as GPIO
from time import sleep
import os 

GPIO.setmode(GPIO.BCM)
sleepTime=0.1

lightPin=4
buttonPin=17

GPIO.setup(lightPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin,False)

try:
	while True:
		#lights up light on press and light off on release
		GPIO.output(lightPin,not GPIO.input(buttonPin))
		if(GPIO.input(buttonPin)):
			os.system('python vision.py')			
		sleep(0.1)
		
finally:
	#will make the light off after the program completes execution
	GPIO.output(lightPin,False)	
	GPIO.cleanup()
