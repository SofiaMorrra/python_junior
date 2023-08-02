import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="zenjulka",
    database="sakila"
)
db.autocommit = True

mycursor = db.cursor()
print(mycursor)

# mycursor.execute("SELECT * FROM student")
# result = mycursor.fetchone()
# print(result)

# result = mycursor.fetchmany(6)
# print(result)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM actor")
result = mycursor.fetchall()
print(result)

mycursor.execute("SELECT * FROM actor WHERE first_name = 'PENELOPE'")
result = mycursor.fetchall()
print(result)



