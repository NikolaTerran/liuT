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

#command = "CREATE TABLE new_roster(code TEXT,mark INTERGER,id INTERGER)"
#c.execute(command)    #run SQL statement

#file = open('data/courses.csv')
#reader = csv.reader(file)
#next(reader)
#for row in reader:
#	command2 = "INSERT INTO new_roster VALUES (?,?,?);"
#	c.execute(command2,row)
	


#==========================================================

#db.commit() #save changes
c.execute("SELECT * FROM new_roster")
print(c.fetchall())
db.close()  #close database



