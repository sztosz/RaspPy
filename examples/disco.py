#!/usr/bin/env python
import random
import threading
import time

import RPi.GPIO as GPIO

red = 17
green = 18
yellow = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)


class LedThread(threading.Thread):
    def __init__(self, gpio):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.gpio = gpio
        self.is_lit = False
        self.is_running = True
        GPIO.output(self.gpio, self.is_lit)

    def run(self):
        while self.is_running:
            t = random.uniform(0, 2)
            time.sleep(t)
            self.is_lit = not self.is_lit
            GPIO.output(self.gpio, self.is_lit)

    def stop(self):
        self.is_running = False


red_thread = LedThread(red)
green_thread = LedThread(green)
yellow_thread = LedThread(yellow)

red_thread.start()
green_thread.start()
yellow_thread.start()

raw_input('\n *******Press ENTER key to stop and quit program******* \n')

red_thread.stop()
green_thread.stop()
yellow_thread.stop()

red_thread.join()
green_thread.join()
yellow_thread.join()

GPIO.cleanup()
