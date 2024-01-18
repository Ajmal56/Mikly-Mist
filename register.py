#!C:\python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")



Form=cgi.FieldStorage()
FName=Form.getvalue("Name")
FProduct=Form.getvalue("Product")
FContact=Form.getvalue("Contact")
FCity=Form.getvalue("City")
print("<br><center><h2>Thank you for Milky Mist online shop<a href='/Milky Mist'><br><br>Back to Home</a<h2></center>")

#print("<h1>",FName,FProduct,FContact,FCity,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Milky Mist"   
    )
mycursor=mydb.cursor()
sql="INSERT INTO customer(Name,Product,Contact,city)VALUES(%s,%s,%s,%s)";
val=(FName,FProduct,FContact,FCity)
mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")


