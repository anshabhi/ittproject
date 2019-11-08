#!/Python/python
# Import modules for CGI handling
import cgi, cgitb
import os
import pymongo
from pymongo import MongoClient
# Create instance of FieldStorage
form = cgi.FieldStorage()
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['local']
ud = db.instructor
myquery = { "name": form["username"].value, "password" : form["password"].value }

mydoc = ud.find(myquery)
#if (len(list(mydoc))):
#    status = "Login Successful"
#else:
#    status = "Login Failed"
# Get data from fields
#cmd = form.getvalue('command')
#a = os.popen(cmd).read()
print ("Content-type:text/html\r\n\r\n")
#print ("<html>")
#print ("<head>")
#print ("<title>Execute Command from Form</title>")
#print ("</head>")
#print ("<body>")
#print (status);
print (len(list(mydoc)))
#print ("<h2>Output:</h2>",form)
#print ("</body>")
#print ("</html>")

