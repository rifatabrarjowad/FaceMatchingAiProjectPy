import base64

from django.shortcuts import render
import numpy as np
import cv2
import face_recognition

def home(request):
    if request.method == 'POST':
        inImg = request.FILES.get["inputImage"].read()

        encoded = base64.b64encode(inImg)
        mime = "image/jpg"
        mime = mime + ";" if mime else ";"
        input_image = "data:%sbase64,%s" % (mime, encoded)
        print(input_image)


        return render(request, "index.html", {{"input_image": input}})

    ## do something with the images
    return render(request, 'index.html')
