#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


db = sqlite3.connect("sp_database") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


#command = "CREATE TABLE roster(name TEXT,userid INTERGER)"
file = open('courses.csv')
reader = csv.DictReader(file)

command2 = ""

for row in reader:
	print(row)
	command2 = "INSERT INTO roster VALUES ('name','userid');"
	c.execute(command2)
	

#c.execute(command)    #run SQL statement
#==========================================================

db.commit() #save changes
c.execute("SELECT * FROM roster")
print(c.fetchall())
db.close()  #close database



