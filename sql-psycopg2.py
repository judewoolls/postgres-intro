import psycopg2

#connect to the database
connection = psycopg2.connect(database="chinook")

#build a cursor object of the database
cursor = connection.cursor()

#fetch results (multiple)
results = cursor.fetchall()

#fetch results (single)
#result = cursor.fetchone()

#close the connection
connection.close()

#prints results
for result in results:
    print(result)