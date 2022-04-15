
import mysql.connector
from mysql.connector import pooling
import sys

class Database:
    def __init__(self):
        # Create some constant values for the pool name and size
        self.POOL_SIZE = 10
        self.POOL_NAME = "mypool"
        
        
        # Create an object with parameters needed for connection
        database_config = {
            'database' : 'user_database',
            'user' : 'root',
            'password' : 'Goutham@1005',
            'host' : 'localhost',
            
        }
        # Create the connection pool.
        self.cnxpool = pooling.MySQLConnectionPool(pool_name = self.POOL_NAME,
                              pool_size = self.POOL_SIZE,
                              auth_plugin='mysql_native_password',
                              **database_config)

    def query(self,select,table, full_string=None):
        if not full_string:
            full_string = "SELECT %s FROM %s" % (select,table)

        cnx  = self.cnxpool.get_connection()

        cursor = cnx.cursor(buffered=True)

        cursor.execute(full_string)

        desc = cursor.description
        column_names = [col[0] for col in desc]

        data = [dict(zip(column_names, row)) for row in cursor.fetchall()]

        cursor.close()

        cnx.close()

        return data

mydbpool = Database()

print(mydbpool.query("*","user_details"))