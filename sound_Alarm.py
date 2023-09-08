from engi1020.arduino.api import *
from time import sleep
import math

def alarm_light():
    sleep(1)
    buzzer_frequency(5, 1000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 1000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 1000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 1000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 1000)
    sleep(1)
    buzzer_stop(5)
    
    
def alarm_temp():
    sleep(1)
    buzzer_frequency(5, 2000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 2000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 2000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 2000)
    sleep(1)
    buzzer_stop(5)
    sleep(1)
    buzzer_frequency(5, 2000)
    sleep(1)
    buzzer_stop(5)
    


