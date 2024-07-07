import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Dj@421421'
)

cursorobject = dataBase.cursor()

cursorobject.execute("CREATE DATABASE restdb")

print("Done !")