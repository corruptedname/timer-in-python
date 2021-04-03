import time, os, random, sys
from time import sleep 
import playsound
hour_timer_user_input = int(input(":::how many hours? set 0 if none:::"))
minutes_timer_user_input = int(input(":::how many minutes? set 0 if none:::"))
seconds_timer_user_input = int(input(":::how many seconds? set 0 if none:::"))
seconds_timer_input = hour_timer_user_input * 60  + minutes_timer_user_input * 60 + seconds_timer_user_input
output_in_hours = seconds_timer_input / 60 / 60
output_in_minutes = seconds_timer_input / 60 
while True:
    os.system('cls')
    if seconds_timer_input >= 0:
        print("time is")
        print(seconds_timer_input)
        print("in seconds")
        print("timer is")
        print(output_in_minutes)
        print("in minutes")
        print("timer is")
        print(output_in_hours)
        print("in hours")
        seconds_timer_input -= 1
        output_in_minutes -= 1 / 60
        output_in_hours -= 1 / 60 / 60 
        time.sleep(1.0)
        os.system('cls')
        continue 
    else:
        print("the timer finished")
        break
