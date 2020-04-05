from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import os
import serial
from gtts import gTTS
import pygame
import time
import random
from video_image import front
from test import prediction
# arduino = serial.Serial('COM9', 9600)



def Index(request):

    return render(request,'index.html')


def Detect(request):
    global flag_dis

    while 1:
        flag_dis = 0;
        # reading from arduino serial monitor

        # data = int(arduino.readline())  # acknowledgement flag
        # data = 1111
        # data = int(arduino.readline())  # acknowledgement flag
        data = 1111
        print(data)

        if data != 0000:
            # Checking person's position
            if data == 1111:
                text = "please move closer by"
            elif data == 2222:
                text = "please move back by"
            else:
                break
            lan = 'en'
            flag_dis=1
            # data2 = int(arduino.readline()) # distance
            data2=6
            print(data2)
            text += str(data2)
            text += "cm"
        else:
            text = "scan starting, please stay still"
            flag_dis = 1

        # lan = 'en'
        # myobj = gTTS(text=text, lang=lan, slow=False)
        # myobj.save("guide.mp3")
        # pygame.mixer.init()
        # pygame.mixer.music.load("guide.mp3")
        # pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy():
        #     time.sleep(20)
        #     #pygame.time.Clock().tick(500)
        # pygame.mixer.music.load("beep.mp3")
        # os.remove("guide.mp3")

        # block of code if person is correctly positioned
        if flag_dis == 1:
            # while 1:
            #     time.sleep(10)
            #     print('.')

            return HttpResponseRedirect(reverse('images'))


    return render(request,'index.html')




def take_images(request):
      v=str(random.randrange(1000,9999))
      data = 0
      # front(str(v))
      # count = prediction(str(v))
      count=2
      if(count>=2):
          text = "You need to be quarantined"
          lan = 'en'
          myobj = gTTS(text=text, lang=lan, slow=False)
          data = 1
          # pygame.mixer.init()
          # pygame.mixer.music.load("guide.mp3")
          # pygame.mixer.music.play()
          # while pygame.mixer.music.get_busy():
          #     time.sleep(20)
          #     # pygame.time.Clock().tick(500)
          # pygame.mixer.music.load("beep.mp3")
          # os.remove("guide.mp3")
          # return render(request,"warning.html")

      return render(request,"index.html",{'data':data})



# def random(request):
#     context={
#     'data':1,
#     }
#     return render(request,'random.html',context)
