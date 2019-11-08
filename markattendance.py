#!/Python/python

import asyncio, io, glob, os, sys, time, uuid, requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
import cgi, cgitb
import os
import pymongo
from pymongo import MongoClient
from datetime import datetime
import cloudinary
import cloudinary.uploader
import base64


form = cgi.FieldStorage();
cloudinary.config( 
  cloud_name = "#", 
  api_key = "#", 
  api_secret = "#" 
)


im2 = form["im2"].value
im2 = im2.split(',')[1]
im2 = im2.replace(' ','+')



imgdata = base64.b64decode(im2)
filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
        f.write(imgdata)
result = cloudinary.uploader.unsigned_upload('some_image.jpg','#')
#print(len(img_data))


url = result['url']
client = MongoClient('mongodb://localhost:27017/')
db = client['local']
ud = db.users
myquery = { "name": form["username"].value }

#myquery = { "name": "root" }
mydoc = ud.find(myquery)
url2 = mydoc[0]['image'];
status = 0
face1 = 1
# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
KEY = '#'  #os.environ['e9c9b7dd2569469a93c936c61a02b7e5']

# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = '#' #os.environ['https://itt-project.cognitiveservices.azure.com/face/v1.0']

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Detect a face in an image that contains a single face
single_face_image_url = url#'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
single_image_name = os.path.basename(single_face_image_url)
detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
print ("Content-type:text/html\r\n\r\n")

if not detected_faces:
    face1 = 0#raise Exception('No face detected from image {}'.format(single_image_name))

# Display the detected face ID in the first single-face image.
# Face IDs are used for comparison to faces (their IDs) detected in other images.
#print('Detected face ID from', single_image_name, ':')
#for face in detected_faces: print (face.face_id)
#print()
try:
    if face1 != 0:
    # Save this ID for use in Find Similar
        first_image_face_ID = detected_faces[0].face_id

        # Detect the faces in an image that contains multiple faces
        # Each detected face gets assigned a new ID
        multi_face_image_url = url2
        multi_image_name = os.path.basename(multi_face_image_url)
        detected_faces2 = face_client.face.detect_with_url(url=multi_face_image_url)

        # Search through faces detected in group image for the single face from first image.
        # First, create a list of the face IDs found in the second image.
        second_image_face_IDs = list(map(lambda x: x.face_id, detected_faces2))
        # Next, find similar face IDs like the one detected in the first image.
        similar_faces = face_client.face.find_similar(face_id=first_image_face_ID, face_ids=second_image_face_IDs)

        if not similar_faces[0]:
            status = 0
        else:
            status = 1
    # Print the details of the similar faces detected 
except:    
    print(0,end='')
    
print(status,end='')    

if status is 1:
    
    at = db.attendance
    ud = db.attendance_live
    myquery = { "subject": form["subject"].value}
    mydoc = ud.find(myquery)
    stat2 = int(mydoc[0]["status"])
    #print(stat2)
    if stat2 is 1:
        now = datetime.now()
        date_time = now.strftime("%c")
        post = {"name": form["username"].value, "subject": form["subject"].value,"time": date_time }
        
        at.insert_one(post)
        print(2,end='')




    
