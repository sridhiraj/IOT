import RPi.GPIO as GPIO
import time

LED_1_PIN = 17
LED_2_PIN = 27
#LED_3_PIN = 22
#BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1_PIN, GPIO.OUT)
GPIO.setup(LED_2_PIN, GPIO.OUT)
#GPIO.setup(LED_3_PIN, GPIO.OUT)
#GPIO.setup(BUTTON_PIN, GPIO.IN)

GPIO.output(LED_1_PIN, GPIO.LOW)
GPIO.output(LED_2_PIN, GPIO.LOW)


'''
while True:
    user_input = input("Enter '1' to continue or any other key to exit: ")
    if user_input == '1':
        GPIO.output(LED_1_PIN, GPIO.HIGH)
    else:
        print("Exiting the program.")
        GPIO.output(LED_1_PIN, GPIO.LOW)
        break
        
 #   GPIO.output(LED_2_PIN, GPIO.HIGH)
  #  GPIO.output(LED_3_PIN, GPIO.HIGH)
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_1_PIN, GPIO.HIGH)
        GPIO.output(LED_2_PIN, GPIO.HIGH)
        GPIO.output(LED_3_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_1_PIN, GPIO.LOW)
        GPIO.output(LED_2_PIN, GPIO.LOW)
        GPIO.output(LED_3_PIN, GPIO.LOW)    
    '''

GPIO.cleanup()

