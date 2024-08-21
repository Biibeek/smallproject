import pygame
import time
CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"

def alarm(sec):
    time_elapsed=0

    while time_elapsed<sec:
        time.sleep(1)
        time_elapsed +=1
        time_left=sec-time_elapsed
        minutes_left=time_left // 60
        seconds_left=time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}", end='', flush=True)
    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')  # Replace 'alarm.mp3' with your actual sound file path
    pygame.mixer.music.play()


    while pygame.mixer.music.get_busy():
        time.sleep(1)

minutes=int(input("enter how many minutes would you like to set an alarm:"))
sec=int(input("enter how many seconds you ll like to set an alarm:"))
total_time=minutes*60+sec
alarm(total_time)