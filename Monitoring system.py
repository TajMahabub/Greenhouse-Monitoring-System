from engi1020.arduino.api import *
from playsound import playsound
from time import sleep
import math
from sound_Alarm import *
from LED_alarm import *

def greenhouse_monitor():
    """A monitoring system with multiple scenario usability, but for our project we devised a system
that specifically monitors plants such as fruits, vegetable, flowers etc... in a greenhouse.
"By Novera(202104170) and Taj(202173258)" """

    ####LIST FOR STORING LIGHT AND TEMPERATURE VALUES CONTINUOUSLY#############
    
    
    list_tempr = []
    lst_light = []
    
    ####################################################################################################
    ###########CREATING DATABASE i.e. dictionary of plants and family and types of each plants##########
    ####################################################################################################


    #######################
    Lili = {'max_temp' : 30.0,
            'min_temp' : 15.0}

    Amary = {'max_temp' : 25.0,
             'min_temp' : 13.0}

    Chenopodi = {'max_temp' : 20.0,
                 'min_temp' : 15.0}

    vege = {1: Lili,
            2: Amary,
            3: Chenopodi}
    #########################


    Parsley = {'max_temp' : 26.7,
               'min_temp' : 10.0}

    Mustard = {'max_temp' : 23.9,
               'min_temp' : 18.3}

    Pea = {'max_temp' : 18.3,
           'min_temp' : 12.8}


    flo = {1: Parsley,
           2: Mustard,
           3: Pea}
    #########################

    Rosa = {'max_temp' : 7.2,
            'min_temp' : 0.0}

    Erica = {'max_temp' : -5.0,
             'min_temp' : -7.0}

    Musa = {'max_temp' : 32.0,
            'min_temp' : 31.0}


    fru = {1: Rosa,
           2: Erica,
           3: Musa}

    ############################
    plants = {'Vegetable' : vege,
              'Flower': flo,
              'Fruits': fru}
    ##################################################################################
    ##################################################################################
    
    ######TAKING IN USER INPUT TO DECIDE WHICH METHOND TO FOLLOW i.e manual or predefined set values########


    user_input = 'K'
    while user_input != "Y" or user_input!= 'N':
        user_input = str(input("Do you want to select from predefined optimal values of plants(Y/N): "))
        if user_input == 'Y':
            max_light = 750
            min_light = 25
            print()
            print("Optimal Light range is:", max_light ,"to", min_light)
            print()
            lst_plants = list(plants.keys())
            print("These are the list of produce...")
            print(lst_plants)
            print()
            family = input("Which type of produce would you like? ")
            if family == 'R' or 'r':
                playsound('C:\\Users\\Alif\\Downloads\\Video\\rick roll.mp3')
            if plants.get(family) == None:
                print("Error!, Please try again")
                continue
            else:
                
                if family == "Vegetable":
                    print("These are the available options for vegetable:")
                    print()
                    print("1: Liliaceae")
                    print("2: Amaryllidaceae")
                    print("3: Chenopodiaceae")
                    print()
        #             option = input(list(plants.get(family).keys()))
                    option = int(input("Enter your desired choice: "))
                    if option == 1:
                        li = list(vege.get(option).values())
                        max_temp = li[0]
                        min_temp = li[1]
                        print("Temperature range is:", max_temp ,"to", min_temp)
                    elif option == 2:
                        li = list(vege.get(option).values())
                        max_temp = li[0]
                        min_temp = li[1]
                        print("Temperature range is:", max_temp ,"to", min_temp)
                    elif option == 3:
                        li = list(vege.get(option).values())
                        max_temp = li[0]
                        min_temp = li[1]
                        print("Temperature range is:", max_temp ,"to", min_temp)
                    else :
                        print("Error!, try again")
                        continue
                    
                    
                elif family == "Flower":
                     print("These are the available options for flower:")
                     print()
                     print("1: Parsley")
                     print("2: Mustard")
                     print("3: Pea")
                     print()
        #             option = input(list(plants.get(family).keys()))
                     option = int(input("Enter your desired choice: "))
                     if option == 1:
                         Pars = list(flo.get(option).values())
                         max_temp = Pars[0]
                         min_temp = Pars[1]
                         print("Temperature range is:", max_temp ,"to", min_temp)
                     elif option == 2:
                         Pars = list(flo.get(option).values())
                         max_temp = Pars[0]
                         min_temp = Pars[1]
                         print("Temperature range is:", max_temp ,"to", min_temp)
                     elif option == 3:
                         Pars = list(flo.get(option).values())
                         max_temp = Pars[0]
                         min_temp = Pars[1]
                         print("Temperature range is:", max_temp ,"to", min_temp)
                     else:
                         print("Error!, try again")
                         continue
                        
                elif family == "Fruits":
                    print("These are the available options for fruit:")
                    print()
                    print("1: Rosaceae")
                    print("2: Ericaceae")
                    print("3: Musaceae")
                    print()
        #             option = input(list(plants.get(family).keys()))
                    option = int(input("Enter your desired choice: "))
                    if option == 1:
                        ros = list(fru.get(option).values())
                        max_temp = ros[0]
                        min_temp = ros[1]
                        print("Temperature range is:", max_temp ,"to", min_temp)
                    elif option == 2:
                        ros= list(fru.get(option).values())
                        max_temp = ros[0]
                        min_temp = ros[1]
                        print("Temperature range is:", max_temp ,"to", min_temp)
                    elif option == 3:
                        ros = list(fru.get(option).values())
                        max_temp = ros[0]
                        min_temp = ros[1]
                        print("Temperature range is:", max_temp ,"to", min_temp)
                    else:
                        print("Error!, try again")
                        continue    
     
            break
        elif user_input == 'N':
            print("You will need to set optimal values of temperature and light yourself")
            print()
            max_temp = float(input("Enter the maximum temperature value: "))
            min_temp = float(input("Enter the minimum temperature value: "))
            print()
            max_light = float(input("Enter the maximum light value(750 optimal highest): "))#750(optimal highest lighting)
            min_light = float(input("Enter the minimum light value(5 optimal lowest): "))#25(optimal lowest lighting)
            break
        else:
            print("Error, Please try again!")
            continue
        
    #######################ACTUAL MONITORING PROCESS#########################
        
    print()
    print("Monitoring started...")
    print("Press button if you want to stop monitoring")
    oled_clear()
    oled_print("Monitoring")
    while digital_read(6) == False:
        
        ###TEMPERATURE###
        tempr = pressure_get_temp()
        if tempr > max_temp:
            oled_clear()
            oled_print("Temperature HIGH!")
            alarm_temp()
            list_tempr.append(tempr)
            break
        elif tempr < min_temp:
            oled_clear()
            oled_print("Temperature LOW!")
            alarm_temp()
            list_tempr.append(tempr)
            break
            
        list_tempr.append(tempr)
        sleep(0.5)
        
        #######LIGHT#########
        
        light = analog_read(6)
        if light > max_light:
            oled_clear()
            oled_print("Light value HIGH!")
            LED_alarm()
            alarm_light()
            lst_light.append(light)
            break
        elif light < min_light:
            LED_alarm()
            oled_clear()
            oled_print("Light value LOW!")
            LED_alarm()
            alarm_light()
            lst_light.append(light)
            break
            
        lst_light.append(light)
        sleep(0.5)
        
    #############FINAL MESSAGE ############
    sleep(2)
    buzzer_stop(5)
    digital_write(4, True)
    oled_clear()
    oled_print("Completed!")
    sleep(3.5)
    digital_write(4, False)
    oled_clear()
    
#     temp = ("Temperature values are:", list_tempr)
#     Light = ('Light values are: ', lst_light)
#     result = (temp, Light)
#     return result
    print("Temperature values are:", list_tempr)
    print('Light values are: ', lst_light)
    
    
    
    
if __name__ == '__main__':
    
    greenhouse_monitor()
