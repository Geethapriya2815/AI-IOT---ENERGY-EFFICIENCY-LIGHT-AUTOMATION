import RPi.GPIO as GPIO
import time

sensor_pin = 18  # GPIO pin for LDR
relay_pin = 23   # GPIO pin for relay

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(relay_pin, GPIO.OUT)

while True:
    sensor_value = GPIO.input(sensor_pin)
    if sensor_value == 0:  # Dark
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn on light
    else:
        GPIO.output(relay_pin, GPIO.LOW)   # Turn off light
    time.sleep(1)
