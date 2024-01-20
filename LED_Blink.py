import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)

#while True:
for i in range(1, 10):
    if i%2 == 0:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
    
GPIO.cleanup()