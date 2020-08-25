import mysql.connector
import sys

cnx = mysql.connector.connect(user = '<user>', 
                              password = '<password>',
                              host = '127.0.0.1',
                              autocommit = True)

cursor = cnx.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS CIS341;")
cursor.execute("CREATE TABLE IF NOT EXISTS CIS341.Word_Count (Word VARCHAR(255), Count INT, PRIMARY KEY (Word));")
cursor.execute("DELETE FROM CIS341.Word_Count;")

for line in sys.stdin:
	line = line.strip()
	word, count = line.split()

	insertion = "INSERT INTO CIS341.Word_Count VALUES ('{}', {});".format(word, count)
	cursor.execute(insertion)

cursor.close()
cnx.close()
