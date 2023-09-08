from engi1020.arduino.api import *
from time import sleep
import math



def LED_alarm():
    
    t_ = True
    f_ = False
    
    digital_write(4, t_)
    sleep(0.8)
    digital_write(4, f_)
    sleep(0.8)
    digital_write(4,t_)
    sleep(0.8)
    digital_write(4, f_)
    sleep(0.8)
    digital_write(4,t_)
    sleep(0.8)
    digital_write(4, f_)
    
    