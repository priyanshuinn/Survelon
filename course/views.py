from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.http.response import StreamingHttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.http import StreamingHttpResponse
from .models import post_data
import multiprocessing
import os
import dlib
from django.views import View
from .centroidtracker import CentroidTracker
from .trackableobject import TrackableObject
from imutils.video import VideoStream
from imutils.io import TempFile
from imutils.video import FPS
from datetime import datetime
from threading import Thread
import numpy as np
import dropbox
import imutils
import dlib
import time
import cv2
import os
import json
from course.camera import VideoCamera
from django.core.files.storage import FileSystemStorage
from .models import upload_file
from course.mask import mask_detect
########################

global speed
speed ="0"
def gen(camera):
    while True:
        frame,s,dt= camera.get_frame()
        global speed
        speed=str(s)+ " MPH"+ "|" + dt
        
        # print(speed)
        yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen_mask(camera):
    while True:
        frame= camera.get_frame()
        yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
# Create your views here.
 
def show(request):
    return render(request,'overview.html')

def overview(request):
    if request.method == 'POST':
        up = request.FILES['document']
        up.name="VIDEO"+"."+up.name.split('.')[1]
        document=upload_file(video = up)
        document.save()
        return redirect('show')

    return render(request, 'upload.html')

def display(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

def even_stream():
    initial_speed=""
    while True:
        global speed
        data=speed
        if not initial_speed == data:
            yield "\ndata: {}\n\n".format(data)
            initial_speed=data
        time.sleep(1)

def load(request):
    return render(request,'mask.html')
def mask(request):
    return StreamingHttpResponse(gen_mask(mask_detect()), content_type='multipart/x-mixed-replace; boundary=frame')

class POSTSpeed(View):
    def get(self,request):
        response=StreamingHttpResponse(even_stream())
        response['Content-Type'] = 'text/event-stream'
        return response

def post(request, my_id):
    data = post_data.objects.get(id=my_id)
    return render(request, 'post.html', {'data': data})
    



    







    
