# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:19:20 2020

@author: Michael Hage
"""

import sql

path = r'url.db'

def retrieve_url(short_id):
    
    # create sql query and fit the variables into it
    query = f"""
        SELECT url FROM url_db
        WHERE short_id = {short_id};
    """
    
    # create sql db connection
    connection = sql.create_connection(path)
    
    # execute query to db
    urls = sql.execute_read_query(connection, query)
    
    return urls

# create short_id within db by using 
def create_short_id(short_id, url):
    
    query = f""" 
        INSERT INTO
            url_db (short_id, url)
        VALUES
            ('{short_id}', '{url}');
        """
    
    connection = sql.create_connection(path)
    
    # execute 
    sql.execute_insert_query(connection, query)
  
# urls = retrieve_url('Ms54Rt')


# create_url = """ 
# INSERT INTO
#     url_db (short_id, url)
# VALUES
#     ('Ms54Rt', 'https://www.google.ca/');
# """

# connection = sql.create_connection(path)

# # error = sql.execute_query(connection, create_url)

# select_url = "SELECT * FROM url_db"

# urls = sql.execute_read_query(connection, select_url)

# for url in urls:
#     print(url)