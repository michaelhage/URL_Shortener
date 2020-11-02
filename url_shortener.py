# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:19:20 2020

@author: Michael Hage
"""

import sql

path = r'url.db'

create_url = """ 
INSERT INTO
    url (short_id, url)
VALUES
    ('Ms54Rt', 'https://www.google.ca/');
"""

connection = sql.create_connection(path)

# error = sql.execute_query(connection, create_url)

select_url = "SELECT * FROM url"

urls = sql.execute_read_query(connection, select_url)

for url in urls:
    print(url)