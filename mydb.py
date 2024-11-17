# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

# import mysql.connector
import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='Ayush1999'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE company")

print("All Done!")
