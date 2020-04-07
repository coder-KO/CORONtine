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
from live_test import predicting_cough
# arduino = serial.Serial('COM9', 9600)
from audio_positioning import arduino_call



def Index(request):

    return render(request,'index.html')


def Detect(request):
    global flag_dis
    arduino_call()

    return HttpResponseRedirect(reverse('images'))


    # return render(request,'index.html')




def take_images(request):
      v=str(random.randrange(1000,9999))
      data = predicting_cough()

    #   front(str(v))
    #   count = prediction(str(v))
    # #   count=2
    #   if(count>=2):
    #       text = "You need to be quarantined"
    #       lan = 'en'
    #       myobj = gTTS(text=text, lang=lan, slow=False)
    #       data = 1
    #       # pygame.mixer.init()
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
