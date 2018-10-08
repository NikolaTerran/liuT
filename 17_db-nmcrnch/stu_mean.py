#Tianrun Liu
#SoftDev1 pd6
#Average
#2018-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect("sp_database.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#
#**************FILL TABLE COURSES********************
#
#open and read csv file
#file = open('data/courses.csv')
#reader = csv.reader(file)
#
#create courses table
#command = "CREATE TABLE courses(code TEXT,mark INTEGER,id INTEGER)"
#c.execute(command)    #run SQL statement
#
#add data by key into table
#for row in reader:
#	command2 = 'INSERT INTO courses VALUES(?,?,?)'
#	c.execute(command2,row)
#
#**************FILL TABLE PEEPS********************
#
#open and read csv file
#file = open('data/peeps.csv')
#new_reader = csv.reader(file)
#
#create peeps table
#command3 = "CREATE TABLE peeps(name TEXT,age INTEGER,id INTEGER)"
#c.execute(command3)
#
#add data by key into table
#for row in new_reader:
#	command4 = 'INSERT INTO peeps VALUES(?,?,?)'
#	c.execute(command4,row)
#
#==========================================================
#
#*************ACCESS STUDENT GRADE*****************
def stu_grade(stu_id):
	c.execute("select name, code, mark from peeps, courses where peeps.id = ? and courses.id = peeps.id",[stu_id])
	result = c.fetchall()
	for r in result:	#https://www.python-course.eu/sql_python.php
		print(r)	
	return ""

def all_stu_grade():
	c.execute("select name, code, mark from peeps, courses where peeps.id = courses.id")
	result = c.fetchall()
	for r in result:	
		print(r)	
	return ""

def stu_average(stu_id):
	c.execute("select mark from courses where courses.id = ?",[stu_id])
	result = c.fetchall()
	i = 0;
	counter = 0;
	for r in result:	
		i += int(r[0])
		counter += 1
	result = int(i/counter)
	print("student with id = " + str(stu_id) + "'s average is " + str(result))	
	return result

#THIS IS NOT WORKING
def all_stu_average():
	c.execute("select name, id from peeps")
	result = c.fetchall()
	for r in result:
		r;
		print(r)
	return ""
#=======================CREATE TABLE peeps_avg============================
#command3 = "CREATE TABLE peeps_avg(id INTEGER,average INTEGER)"
#c.execute(command3)
#
#command4 = "INSERT INTO peeps_avg(id) select id from peeps"
#c.execute(command4)
#
#########################################################################
#USE MODULAR DESIGN#USE MODULAR DESIGN#USE MODULAR DESIGN
#########################################################################
#c.execute("update peeps_avg set average = 'average' where id = 'id'")
#c.execute("update peeps_avg set average = ? where id = 1",[stu_average(1)])
#c.execute("update peeps_avg set average = ? where id = 2",[stu_average(2)])
#c.execute("update peeps_avg set average = ? where id = 3",[stu_average(3)])
#c.execute("update peeps_avg set average = ? where id = 4",[stu_average(4)])
#c.execute("update peeps_avg set average = ? where id = 5",[stu_average(5)])
#c.execute("update peeps_avg set average = ? where id = 6",[stu_average(6)])
#c.execute("update peeps_avg set average = ? where id = 7",[stu_average(7)])
#c.execute("update peeps_avg set average = ? where id = 8",[stu_average(8)])
#c.execute("update peeps_avg set average = ? where id = 9",[stu_average(9)])
#c.execute("update peeps_avg set average = ? where id = 10",[stu_average(10)])
#
#c.execute("delete from peeps_avg where id IS NULL ")
#
#db.commit()
#===========================================================================
		

print("=======================DEMO fetch student grade==================");
stu_grade(1)
print("=======================DEMO fetch all student grade==============");
all_stu_grade()
print("=======================DEMO calc student average=================");
stu_average(1)
print("=======================DEMO all student average==================");
all_stu_average()

#db.commit() #save changes #test code
#print("**************************COURSES*********************************")
#c.execute("SELECT * FROM courses")
#print(c.fetchall())
#print("**************************PEEPS*********************************")
#c.execute("SELECT * FROM peeps")
#print(c.fetchall())
#print("*************************PEEPS_AVG**********************************")
#c.execute("SELECT * FROM peeps_avg")
#print(c.fetchall())
db.close() #close database
