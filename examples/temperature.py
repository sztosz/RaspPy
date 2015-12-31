#!/usr/bin/env python
import threading
import time

from w1thermsensor import W1ThermSensor


class TempThread(threading.Thread):
    def __init__(self):
        super(TempThread, self).__init__()
        self.sensor = W1ThermSensor()
        self.is_running = True
        self.setDaemon(True)

    def run(self):
        while self.is_running:
            print('Temperature {} degree Celcius'.format(
                self.sensor.get_temperature()
            ))
            time.sleep(0.5)

    def stop(self):
        self.is_running = False


temp_thread = TempThread()
temp_thread.start()

raw_input('\n *******Press ENTER key to stop and quit program******* \n')

temp_thread.stop()
temp_thread.join()
