#Tianrun Liu
#SoftDev1 pd6
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect("sp_database") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#command = "CREATE TABLE courses(code TEXT,mark INTERGER,id INTERGER)"
#c.execute(command)    #run SQL statement

#**************FILL TABLE COURSES********************

#file = open('data/courses.csv')
#reader = csv.reader(file)
#next(reader)
#for row in reader:
#	command2 = "INSERT INTO courses VALUES (?,?,?);"
#	c.execute(command2,row)

#command3 = "create table peeps(name TEXT,age INTERGER,id INTERGER)"
#c.execute(command3)

#**************FILL TABLE PEEPS********************

#file = open('data/peeps.csv')
#new_reader = csv.reader(file)
#next(new_reader)
#for row in new_reader:
#	command4 = "INSERT INTO peeps VALUES (?,?,?);"
#	c.execute(command4,row)

#==========================================================

#db.commit() #save changes
print("***********************************************************")
c.execute("SELECT * FROM courses")
print(c.fetchall())
print("***********************************************************")
c.execute("SELECT * FROM peeps")
print(c.fetchall())
print("***********************************************************")
db.close()  #close database



