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
# from video_image import front
#import pyrebase

#


def Index(request):
    # arduino = serial.Serial('COM9', 9600)
    #
    # global flag_dis,flag_angle
    #
    # while(1):
    #     data = str(arduino.readline()) #reading from arduino serial monitor
    #     #assuming distance
    #     if(data<=1.5):
    #         #desired distance
    #         flag_dis=1
    #         return redirect()
    #
    #     else:
    #         text = "move closer"
    #         lan='en'
    #
    #         myobj = gTTS(text=text,lang=lan,slow=False)
    #         myobj.save("hello.mp3")
    #         os.system("mpg321 hello.mp3")
    #
    return render(request,'index.html')


def take_images(request):
      front(str(id))
