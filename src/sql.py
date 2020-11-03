# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:28:52 2020

@author: Michael Hage
"""

import sqlite3
from sqlite3 import Error

# create connection to sql database based off path
def create_connection(path):
    connection = None
    
    # use connect() to connect to the db in the path
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB Successful")
    
    # catches an exception in the case that connect() failes to establish a connection
    except Error as e:
        print(f"the error '{e}' has occured")
        
    return connection

# execute a SQL query to the connection db
def execute_insert_query(connection, query):
    
    # create error in case of abort
    # error = 0
    
    # create cursor to execute query command from connected db
    cursor = connection.cursor()
    
    # execute query
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' has occured")
        
        # if abort happens, then change to error code
        # error = 1
        # print(error)
        # return error

    # return error

def execute_read_query(connection, query):
    
    # create cursor and result
    cursor = connection.cursor()
    result = None
    
    # error = 0
    
    try:
        
        # execute query
        cursor.execute(query)
       
        # retrieve result information
        result = cursor.fetchall()
        return result
    
    except Error as e:
        print(f"The error '{e}' has occured")
        # error = 2