from numpy import append
import snowflake.connector as sf
import snowflake.connector.pandas_tools as sfp
from snowflake.connector.pandas_tools import pd_writer
import pandas as pd
from sqlalchemy import create_engine

conns = {'SnowflakeDB': {'UserName': 'Boinegoutham10',
                         'Password': 'Goutham@1005', 'Host': 'UE41703.ap-south-1'}}


# conn = create_engine(
#     "snowflake://Boinegoutham10:Goutham@1005@localhost/customer_data/compute_wh")

conn = sf.connect(
    user = conns['SnowflakeDB']['UserName'],
    password = conns['SnowflakeDB']['Password'],
    account = conns['SnowflakeDB']['Host']
)

print(conn)
# conn = sf.connect(
#     user='Boinegoutham10',
#     password='Goutham@1005',
#     account='UE41703.ap-south-1',
#     warehouse='compute_wh',
#     database='customer_data',
# )

df = pd.DataFrame([('Goutham', '10'), ('Sunny', '20')],
                  columns=['name', 'balance'])

conn.cursor().execute("use database customer_data")
conn.cursor().execute("use schema public")


# temp= sfp.write_pandas(conn, df, 'customers', quote_identifiers=False)

# print(temp)
# temp= sfp.write_pandas(conn, df, 'customers', quote_identifiers=False)

# we can also write as
# success, nchunks, nrows, _ = sfp.write_pandas(conn, df, 'customers', quote_identifiers=False)

# success will give us true/false
# nchunks will give us count
# nrows will give us count of no of rows inserted
# _ gives us the detailed info

# df.to_sql('customers', con=conn, index=False, method=pd_writer)
sql = (
    "create or replace table product (name string, balance string)"
)

conn.cursor().execute(sql)
df.to_sql('product', con=conn, index=False, method= pd_writer, if_exists='append')  #error in this line.. check and solve it    