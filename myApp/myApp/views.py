import base64

from django.shortcuts import render
import numpy as np
import cv2
import face_recognition

def home(request):
    if request.method == 'POST':

        # Get the uploaded image files from the form
        inImg = request.FILES['firstImg']
        inImg2 = request.FILES['secondImg']

        # Load and process the first image
        imgElong = face_recognition.load_image_file(inImg)
        imgElong = cv2.cvtColor(imgElong, cv2.COLOR_BGR2RGB)

        # Load and process the second image
        imgTest = face_recognition.load_image_file(inImg2)
        imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)


        # Locate and encode the face in the first image
        faceLoc = face_recognition.face_locations(imgElong)[0]
        encodeElong = face_recognition.face_encodings(imgElong)[0]

        # Locate and encode the face in the second image
        faceLocTest = face_recognition.face_locations(imgTest)[0]
        encodeElongTest = face_recognition.face_encodings(imgTest)[0]

        # Compare faces and calculate face distance
        Results = face_recognition.compare_faces([encodeElong], encodeElongTest)
        faceDis = face_recognition.face_distance([encodeElong], encodeElongTest)
        print(Results, faceDis)


        return render(request, "index.html")

    ## do something with the images
    return render(request, 'index.html')
