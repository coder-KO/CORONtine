import serial
import pygame
import time

def play(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(10)
    pygame.mixer.music.load("../hardware/audio-files/beep.mp3")


def arduino_call():
    arduino = serial.Serial('COM9', 9600)

    while 1:
        print(int(arduino.readline()))

        if abs(int(arduino.readline()) - 20) >= 3:
            while abs(int(arduino.readline()) - 20) >= 3:
                if int(arduino.readline()) > 20:
                    print(int(arduino.readline()))
                    play('../hardware/audio-files/guide1.mp3')
                elif int(arduino.readline()) < 20:
                    print(int(arduino.readline()))
                    play('../hardware/audio-files/guide2.mp3')
        else:
            print(int(arduino.readline()))
            play('../hardware/audio-files/guide3.mp3')
            break

