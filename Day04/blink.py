# LED 깜빡이기
import RPi.GPIO as GPIO
import time

signal_pin =18

#GPIO.setmode(GPIO.BOARD) # 1~40
GPIO.setmode(GPIO.BCM) #GPIO 18, GND
GPIO.setup(signal_pin, GPIO.OUT) #GPIO 18핀에다가 출력을 설정

while (True):
    GPIO.output(signal_pin, True) # GPIO 18핀에 전압시그널 ON
    time.sleep(2) # 2초동안 불킴
    GPIO.output(signal_pin, False) # GPIO 18핀에 전압시그널 OFF
    time.sleep(1) # 1초동안 불끔  