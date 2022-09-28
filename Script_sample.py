# -*- coding: utf-8 -*-

import json
import mysql.connector
from mysql.connector import Error

'''
you can modify the parameters of connection 
which are the host name, your user name, your password and the data base
you can also modify the request in line 58 to 77.
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
        print("MySQL Database connection successful")
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

with open('C:/Users/IBRAHIMA/Downloads/taxon work/taxon work/hse_pathogens.bacteria_w_taxa.json') as mf1:
    bacteria = json.load(mf1)

with open('C:/Users/IBRAHIMA/Downloads/taxon work/taxon work/hse_pathogens.fungi_w_taxa.json') as mf2:
    fungi = json.load(mf2)

with open('C:/Users/IBRAHIMA/Downloads/taxon work/taxon work/hse_pathogens.helminths_w_taxa.json') as mf3:
    helminths = json.load(mf3)

with open('C:/Users/IBRAHIMA/Downloads/taxon work/taxon work/hse_pathogens.protozoa_w_taxa.json') as mf4:
    protozoa = json.load(mf4)


query = """
SELECT *
FROM sample where 
"""
for i in range(len(bacteria)):
    query += """ tax_id = """ +str(bacteria[i]["taxon_id"])+""" OR """

for i in range(len(fungi)):
    query += """ tax_id = """ +str(fungi[i]["taxon_id"])+""" OR """

for i in range(len(helminths)):
    query += """ tax_id = """ +str(helminths[i]["taxon_id"])+""" OR """


for i in range(len(protozoa)):
    query += """ tax_id = """ +str(protozoa[i]["taxon_id"])
    if i < len(protozoa):
        query += """ OR """

query += """ ; """

results = read_query(connection, query)

result = open("C:/Users/IBRAHIMA/Downloads/taxon work/taxon work/result_PATOGENE.tsv","w")

for i in results:
  result.write(i+"\n")








