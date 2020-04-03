import os
import serial
import pygame
import time
from gtts import gTTS


arduino = serial.Serial('COM9', 9600)

global flag_dis

while 1:
    flag_dis = 0;
    # reading from arduino serial monitor
    data = int(arduino.readline())  # acknowledgement flag
    print(data)

    if data != 0000:
        # Checking person's position
        if data == 1111:
            text = "please move back by"
        elif data == 2222:
            text = "please move back by"
        else:
            break
        lan = 'en'
        # flag_dis=1
        data2 = int(arduino.readline()) # distance
        print(data2)
        text += str(data2)
        text += "cm"
    else:
        text = "scan starting, please stay still"
        flag_dis = 1

    lan = 'en'
    myobj = gTTS(text=text, lang=lan, slow=False)
    myobj.save("guide.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("guide.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(5)
        #pygame.time.Clock().tick(500)
    pygame.mixer.music.load("beep.mp3")
    os.remove("guide.mp3")

    # block of code if person is correctly positioned
    if flag_dis == 1:
        while 1:
            time.sleep(10)
            print('.')


