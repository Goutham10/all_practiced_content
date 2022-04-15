
import pandas as pd

from sqlalchemy import create_engine



#this is one way of accessing the DB with python 
#but we dont get column names after retriving the db into python

# we have a disadvantage in this approach is that we have to explicity write the column names by ourselves

# DB_HOST = "localhost"
# DB_NAME = "postgre_flask"
# DB_USER = "postgres"
# DB_PASS = "sunny123"

# con = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)


# cur = con.cursor()
# cur.execute("select * from user_details")
# rows = cur.fetchall()

# df = pd.DataFrame(rows, columns=["id", "name", "phone", "email"])
# print(df)


#second way of approach

dbString = "postgresql://postgres:sunny123@localhost:5432/postgre_flask"

connection = create_engine(dbString).connect()

df = pd.read_sql_table("user_details", connection)

print(df)


# doing operations by using the second way approach
# id = 4
# name = "sunny"
# phone = 4444
# email= "sunny@gmail.com"

# query = "INSERT INTO user_details (id, name, phone, email) VALUES ({},{},{},{})".format(id, name, phone,email)

# df1 = pd.read_sql_query(query, connection)

# df1.to_sql(   
#     name="user_details",
#     con= connection,
#     index=False,
#     if_exists="append"
# )

# print(df1)