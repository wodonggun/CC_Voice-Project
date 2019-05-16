import keyboard             #Using module keyboard
import time                 #sleep 사용 
while True:                 #making a loop
    print("hello")
    time.sleep(0.1)
    if keyboard.is_pressed('UP'): #if key 'a' is pressed 
        print('UP KEY PRESS')
    elif keyboard.is_pressed("p"):
        print("p KEY PRESS")
    else: 
        pass
