# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import Error

'''
you can modify the parameters of connection 
which are the host name, your user name, your password and the data base
you can also modify the request in line 45.
The result of the query will be saved in a TSV file
'''
HostName = "localhost"
Root = "root"
PassWord = "pass"
DataBase = "test"

def db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = db_connection(HostName, Root, PassWord,DataBase)
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


query = """SELECT * FROM expression; """
results = read_query(connection, query)

result = open("C:/Users/IBRAHIMA/Downloads/taxon work/taxon work/result_COVID-19.tsv","w")

for i in results:
  result.write(i+"\n")







