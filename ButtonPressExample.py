import RPi.GPIO as GPIO
import time

LED_1_PIN = 17
LED_2_PIN = 27
BUTTON_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_1_PIN, GPIO.OUT)
GPIO.setup(LED_2_PIN, GPIO.OUT)
led_index = 0
while True:
    time.sleep(0.01)
    #print(GPIO.input(BUTTON_PIN))
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        ##Now we have to decide which light to lit.
        if led_index == 0:
            GPIO.output(LED_1_PIN, GPIO.HIGH)
            GPIO.output(LED_2_PIN, GPIO.LOW)
            led_index=1;
        elif led_index==1:
            GPIO.output(LED_1_PIN, GPIO.LOW)
            GPIO.output(LED_2_PIN, GPIO.HIGH)
            led_index=0
    #time.sleep(0.5)

GPIO.cleanup()