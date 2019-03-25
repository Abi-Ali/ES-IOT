import RPi.GPIO as GPIO
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

dhtPin = dht11.DHT11(pin=33)

while True:
    dhtValue = dhtPin.read()
    
    if dhtValue.is_valid():
        print("Temp : %d C" % dhtValue.tempereture)
        print("Humidity : %d %%" % dhtValue.humidity)


    time.sleep(1)

    GPIO.cleanup()
