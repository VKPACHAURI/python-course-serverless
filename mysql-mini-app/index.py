import mysql.connector

my_connection=mysql.connector.connect(
    host="47.128.247.212",
    user="peter",
    passwd="Radhey@123"
)

print(my_connection)