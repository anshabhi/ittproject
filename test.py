#!/Python/python
import cgi,cgitb
import cloudinary
import cloudinary.uploader
import base64
import re

form = cgi.FieldStorage();
cloudinary.config( 
  cloud_name = "dosluptl1", 
  api_key = "814511136148816", 
  api_secret = "316_9PrlzU7o-Ju4QvA7XAE4US8" 
)

im1 = form["im1"].value
im2 = form["im2"].value
im2 = im2.split(',')[1]
im2 = im2.replace(' ','+')

#img_data = im1 + ';' + im2


imgdata = base64.b64decode(im2)
filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
        f.write(imgdata)
result = cloudinary.uploader.unsigned_upload('some_image.jpg','wmjzcjrx')
#print(len(img_data))
print ("Content-type:text/html\r\n\r\n")
print (result['url'])

