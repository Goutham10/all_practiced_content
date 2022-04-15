import os
import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database = "postgre_flask",
    user = os.environ['DB_USERNAME'],
    password = os.environ['DB_PASSWORD'])
    
cur = con.cursor()
cur.execute("CREATE TABLE user_details( id INTEGER PRIMARY KEY, name varchar(150) NOT NULL, phone INTEGER NOT NULL, email TEXT);")

cur.execute('INSERT INTO user_details (id, name, phone, email)'
            'VALUES (%s, %s, %s, %s)',
            (123,
             'Charles',
             4897878,
             'charles@gmail.com')
            )
        
con.commit()
cur.close()
con.close()