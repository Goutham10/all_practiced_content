import logging
import os
import snowflake.connector as sf
from dotenv import load_dotenv

load_dotenv()


class python_veritas_base:

    def __init__(self, p_log_file_name = None):
        filename = p_log_file_name
        if filename is None:
            filename = '/home/vy/snowflake_practice/sf_python_connector.log'

        logging.basicConfig(
            filename=filename,
            level=logging.INFO
        )


    def create_connection(self):

        conn = sf.connect(
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            account = os.getenv('ACCOUNT'),
            warehouse = os.getenv('WAREHOUSE'),
            database = os.getenv('DATABASE')
            # user='Boinegoutham10',
            # password='Goutham@1005',
            # account='UE41703.ap-south-1',
            # warehouse='compute_wh',
            # database='customer_data'
        )
        
        return conn

    def create_warehouse_database_and_schema(self, conn):
        print("**** creating warehuse, database, schema ****")
        conn.cursor().execute("create warehouse if not exists tiny_warehouse_mg")
        conn.cursor().execute("create database if not exists testdb_mg")
        conn.cursor().execute("use database testdb_mg")
        conn.cursor().execute("create schema if not exists testschema_mg")

        conn.cursor().execute("USE WAREHOUSE tiny_warehouse_mg")
        conn.cursor().execute("USE DATABASE testdb_mg")
        conn.cursor().execute("USE SCHEMA testdb_mg.testschema_mg")


    def set_up(self, connection):
        self.create_warehouse_database_and_schema(connection)
    
    def do_the_real_work(self, conn):
        
        cursor1 = conn.cursor()

        command = "select PI()"

        cursor1.execute(command)

        for row in cursor1:
            print(row)
        
        cursor1.close()
    
    def drop_warehouse_database_and_schema(self, conn):
        conn.cursor().execute("DROP SCHEMA IF EXISTS testschema_mg")
        conn.cursor().execute("DROP DATABASE IF EXISTS testdb_mg")
        conn.cursor().execute("DROP WAREHOUSE IF EXISTS tiny_warehouse_mg")

    def clean_up(self, conn):
        self.drop_warehouse_database_and_schema(conn)

    def main(self):
        
        connection = self.create_connection()
        print(connection)
        
        self.set_up(connection)

        self.do_the_real_work(connection)

        self.clean_up(connection)

        connection.close()

if __name__ == "__main__":
    pvb = python_veritas_base()
    pvb.main()

        