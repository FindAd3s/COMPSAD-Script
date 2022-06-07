import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "testTable"
)

print(mydb)

# cursor = mydb.cursor()

# cursor.execute("select * from tableTest")
# result = cursor.fetchall()

# for x in result:
#     print(x)

# cursor.execute("")
# for x in cursor:
#     print(x)