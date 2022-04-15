import snowflake.connector as sf
from snowflake.connector import DictCursor
import pandas as pd
import time
from codecs import open
import logging
# from config import config

logger = logging.getLogger("app details")
logging.basicConfig(
    filename="/home/vy/snowflake_practice/apps.log",
    level=logging.INFO,
    filemode="w",
    format="%(asctime)s p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)

context = sf.connect(
    user='Boinegoutham10',
    password='Goutham@1005',
    account='UE41703.ap-south-1',
    warehouse='compute_wh',
    database='customer_data'
)

# print(context)

cs = context.cursor(DictCursor)
try:
    print()

    with sf.connect(
        user='Boinegoutham10',
        password='Goutham@1005',
        account='UE41703.ap-south-1',
        warehouse='compute_wh',
        database='customer_data'
    ) as con:
        a = con.cursor().execute("select * from data").fetch_pandas_all()
        print(a['NAME'])
        logger.info(a)
        
    # with open('/home/vy/Downloads/test.sql', 'r') as f:   #to fetch data from external file
    #     for cur in context.execute_stream(f):
    #         for res in cur:
    #             print(res)
    # cs.execute("select * from data")
    # cs.describe("select * from data")
    # print(','.join([col.name for col in cs.description]))
    # print(','.join([col[0] for col in cs.description]))
    # res = cs.fetchall()
    # res = cs.fetch_arrow_all()
    # res = cs.fetch_arrow_batches()
    # res = cs.fetch_pandas_all()
    # res = cs.fetch_pandas_batches()

    # for i in res:
    #     print(i)
    # rows_to_insert = [ (5, 'Vinith', 'Madhapur'), (6, 'dharma', 'durgam cheruvu')]
    # cs.executemany("insert into data(cust_key, name, address) values(%s,%s,%s)",rows_to_insert)

    # print("inserted")
    # cs.execute("select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER limit 10")
    # cs.execute("use customer_Data")
    # cs.execute("select * from data;")
    # df = cs.fetchall()
    # for i in df:
    #     print(i)

    # cs.execute("create or replace table test_table(id integer, name string)")
    # cs.execute("insert into test_table(id, name) values" +
    #            "(123, 'test_string')," +
    #            "(456, 'test_string1')")
    # q1 = cs.sfqid
    # cs.execute(r"select system$cancel_query('q1')")
    # res = cs.fetchall()
    # print(q1)
    # print(len(res))
    # print(res[0])
    # cs.execute_async('select * from test_table')

    # q1 = cs.sfqid
    # print(context.get_query_status(q1))
    # cs.close()
    # context.close()

    # new_conn = sf.connect(user='Boinegoutham10',
    #                       password='Goutham@1005',
    #                       account='UE41703.ap-south-1',
    #                       warehouse='compute_wh',
    #                       database='customer_data')
    # new_cur = new_conn.cursor()

    # new_cur.get_results_from_sfqid(q1)
    # result = new_cur.fetchall()
    # print(result)
    # print(context.get_query_status_throw_if_error(cs.sfqid))

    # while context.is_still_running(context.get_query_status_throw_if_error(cs.sfqid)):
    #     time.sleep(1)
    # df1 = cs.fetchall()
    # for i in df1:
    #     print(i)

    # cs.execute('put file:///home/vy/Downloads/Sample_Superstore* @%test_table')
    # cs.execute('copy into test_table')
    # print("task completed")
except sf.errors.ProgrammingError as e:
    print(e)
finally:
    cs.close()


# def execute_query(connection, query):
#     cursor = connection.cursor()
#     cursor.execute(query)
#     cursor.close()

# try:
#     sql = 'use {}'.format(config.database)
#     execute_query(conn, sql)

#     sql = 'use warehouse {}'.format(config.warehouse)
#     execute_query(conn,sql)

#     sql = 'select * from weather'
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     for r in cursor:
#         print(r)
# except Exception as e:
#     print(e)
