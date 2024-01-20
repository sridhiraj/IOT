import RPi.GPIO as GPIO
import time

LED_1_PIN = 17
BUTTON_PIN = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN)
GPIO.setup(LED_1_PIN, GPIO.OUT)
button_state = GPIO.input(BUTTON_PIN)


'''
GPIO.output(LED_1_PIN,GPIO.LOW)

while True:
    print(button_state)
    if button_state == GPIO.HIGH:
        GPIO.output(LED_1_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_1_PIN,GPIO.LOW)
'''
GPIO.cleanup()