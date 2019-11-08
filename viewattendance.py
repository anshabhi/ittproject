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
myquery = { "name": form["username"].value}

mydoc = ud.find(myquery)

print ("Content-type:text/html\r\n\r\n")
print("<table id = 'result' class='table table-striped table-bordered' style='width:100%'>")
print("<thead><tr><th>Subject</th><th>Date</th></tr></thead><tbody>")
for i in mydoc:
    print ("<tr><td>",i["subject"],"</td><td>",i["time"],"</td></tr>")
print ("</tbody><tfoot><tr><th>Subject</th><th>Date</th></tr></tfoot></table>")    




