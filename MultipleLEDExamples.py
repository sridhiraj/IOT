import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_LIST = [[17, 'OUT'],[27, 'OUT'],[22, 'OUT'],[26, 'IN']]

def GPIOSetup(LED):
	print(LED[0], GPIO.OUT if LED[1] == 'OUT' else GPIO.IN)
	GPIO.setup(LED[0], GPIO.OUT if LED[1] == 'OUT' else GPIO.IN)
	#GPIO.output(LED[0], GPIO.LOW)

for LED in LED_LIST:
	GPIOSetup(LED)


previous_button_state = GPIO.input(LED_LIST[3][0])
led_index=0

while True:
	time.sleep(0.01)
	button_state = GPIO.input(LED_LIST[3][0])
	if button_state != previous_button_state:
		previous_button_state = button_state
		if button_state == GPIO.HIGH:
			if led_index == 0:
				GPIO.output(LED_LIST[0][0], GPIO.HIGH)			
				GPIO.output(LED_LIST[1][0], GPIO.LOW)
				GPIO.output(LED_LIST[2][0], GPIO.LOW)
				led_index=1
			elif led_index == 1:
				led_index=2
				GPIO.output(LED_LIST[0][0], GPIO.LOW)
				GPIO.output(LED_LIST[1][0], GPIO.HIGH)
				GPIO.output(LED_LIST[2][0], GPIO.LOW)
			else:
				GPIO.output(LED_LIST[0][0], GPIO.LOW)
				GPIO.output(LED_LIST[1][0], GPIO.LOW)
				GPIO.output(LED_LIST[2][0], GPIO.HIGH)
				led_index=0
					
GPIO.cleanup()