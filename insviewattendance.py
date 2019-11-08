#!/Python/python
# Import modules for CGI handling
import cgi, cgitb
import os
import pymongo
from pymongo import MongoClient
# Create instance of FieldStorage
form = cgi.FieldStorage()

client = MongoClient('mongodb://localhost:27017/')
db = client['local']
ud = db.attendance
#myquery = {()}

mydoc = ud.find()

print ("Content-type:text/html\r\n\r\n")
print("<table id = 'result' class='table table-striped table-bordered' style='width:100%'>")
print("<thead><tr><th>Name</th><th>Subject</th><th>Date</th></tr></thead><tbody>")
for i in mydoc:
    print ("<tr><td>",i["name"],"</td><td>",i["subject"],"</td><td>",i["time"],"</td></tr>")
print ("</tbody><tfoot><tr><td>Name</td><td>Subject</td><td>Date</td></tr></tfoot></table>")    




