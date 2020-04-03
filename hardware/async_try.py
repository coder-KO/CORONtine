import os
import serial
import pygame
import time
from gtts import gTTS
import random
global data

def speak(text):
    lan = 'en'
    myobj = gTTS(text=text, lang=lan, slow=False)
    myobj.save("guide.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("guide.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(5)
        # pygame.time.Clock().tick(500)
    pygame.mixer.music.load("beep.mp3")
    os.remove("guide.mp3")


arduino = serial.Serial('COM9', 9600)
min_distance = 40
detection_distance = 25
print("starting system with detection range"+str(min_distance)+"cm, and detection distance"+str(detection_distance)+"cm")


while 1:
    person_flag = 0
    data = str(arduino.readline())  # acknowledgement flag
    print(data)
    time.sleep(5)

    # data = random.randrange(10,40)
    # print(data)
    # if data > detection_distance:
    #     print("move closer by "+str(data-detection_distance))
    # elif data < detection_distance:
    #     print("move back by" + str(detection_distance - data))
    # else:
    #     print("right position")
    #     break
    # time.sleep(8)
    # new_data = int(arduino.readline())  # acknowledgement flag
    # print("--->"+str(new_data))

print("Scan starting")


'''
            # new_data = int(arduino.readline())
            while person_flag != 1:
                new_data = int(arduino.readline())
                print(new_data)
                if new_data < detection_distance:
                    speak("please move back by"+str(detection_distance - new_data)+"cm")
                    # new_data = int(arduino.readline())
                elif new_data > detection_distance:
                    speak("please move closer by" + str(new_data - detection_distance) + "cm")
                    # new_data = int(arduino.readline())
                else:
                    person_flag = 1
                print("--->" + str(new_data))
                print(person_flag)
                time.sleep(5)
'''
