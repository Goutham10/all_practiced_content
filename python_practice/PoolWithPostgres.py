from  psycopg2 import pool
import psycopg2


# conn = psycopg2.connect(user='postgres', password='sunny123', database='postgre_flask',host='localhost')
# print(conn)

conn_pool = pool.SimpleConnectionPool(  1,
                                        20,
                                        database='postgre_flask',
                                        user='postgres',
                                        password='sunny123',
                                        host='localhost'
                                        )

if conn_pool:
    print("Connection pool created sucessfully")

ps_connection = conn_pool.getconn()

if ps_connection:
    print("successfully recieved connection from connection pool")

    ps_cursor = ps_connection.cursor()
    ps_cursor.execute("insert into user_details(id, name, phone, email) values(555, 'ramya', 98766545, 'ramya@gmail.com') ")
    ps_connection.commit()
    details = ps_cursor.execute('select * from user_details;')
    user_details = ps_cursor.fetchall()

    print("displaying rows from user details")
    for row in user_details:
        print(row)
    
    ps_cursor.close()

    conn_pool.putconn(ps_connection)
    print("put away a postgresql connection")
