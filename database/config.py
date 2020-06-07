import mysql.connector

def dbconnect():
	try:
		c = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "med_record")
		return c
	except:
		print("Database Connection Error")
		exit(1)