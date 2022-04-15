import mysql.connector.pooling
import sqlalchemy
from sqlalchemy import create_engine

# conn = mysql.connector.connect( host = 'localhost',
#                                 database = 'user_database', 
#                                 user = 'root', 
#                                 password = 'Goutham@1005', 
#                                 auth_plugin='mysql_native_password'
#                             )

# print(conn)
database_config = {
    'database' : 'user_database',
    'user' : 'root',
    'password' : 'Goutham@1005',
    'host' : 'localhost',
    'auth_plugin' : 'mysql_native_password'
}

try:
    conn = mysql.connector.pooling.MySQLConnectionPool( 
                                                        pool_name='new_connection',
                                                        pool_size= 10,#a pool size is a number of the connection objects that the pool can support. If this argument is not given, the default is 5. The pool size cannot be 0 or less than 0.
                                                        pool_reset_session=True, #Reset session variables when the connection is returned to the pool
                                                        **database_config
                                                    )

    
except Exception as e:
    print(e)
    

no_of_connections = [
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
conn.get_connection(),
]


while len(no_of_connections) > conn.pool_size:
    for i in no_of_connections:
        cursor = i.cursor(dictionary = True)

        cursor.execute('select * from user_details where id = 1;')

        for row in cursor:
            print(row)
else:
    print("testing")
# if conn.pool_size :
#         print("entered 11 th connection established")


# print(conn.pool_size)







# db = conn.get_connection()
# db1 = conn.get_connection()
# db2 = conn.get_connection()
# db3 = conn.get_connection()
# db4 = conn.get_connection()
# db5 = conn.get_connection()
# db6 = conn.get_connection()
# db7 = conn.get_connection()
# db8 = conn.get_connection()
# db9 = conn.get_connection()
# db10 = conn.get_connection()
# db11 = conn.get_connection()









# print(conn.pool_name, conn.pool_size)

# conn_obj = conn.get_connection()

# if conn_obj.is_connected():
#     db_info = conn_obj.get_server_info()
#     print("Connected to MySQL database using connection pool", db_info)

#     cursor = conn_obj.cursor()
#     cursor.execute("select database();")
#     record = cursor.fetchone()
#     print("Your connected to - ", record)

