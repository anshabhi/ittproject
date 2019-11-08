#!/Python/python
# Import modules for CGI handling
import cgi, cgitb
import cloudinary
import cloudinary.uploader
import os
import pymongo
from pymongo import MongoClient
import base64
# Create instance of FieldStorage
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
        
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['local']
ud = db.users
post = {"name": form["username"].value, "password": form["password"].value,"image": result["url"]}
status = 1
try:
  ud.insert_one(post)
except:
  status = 0

# Get data from fields
#cmd = form.getvalue('command')
#a = os.popen(cmd).read()
print ("Content-type:text/html\r\n\r\n")
#print ("<html>")
#print ("<head>")
#print ("<title>Execute Command from Form</title>")
#print ("</head>")
#print ("<body>")
print (status)
#print ("<h2>Output:</h2>",form)
#print ("</body>")
#print ("</html>")

