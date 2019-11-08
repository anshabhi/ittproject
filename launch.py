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
ud = db.attendance_live
mydoc = ud.update_one({
  'subject': form["subject"].value
},{
  '$set': {
    'status': form["status"].value
  }
}, upsert=False)

print ("Content-type:text/html\r\n\r\n")
print (1)
