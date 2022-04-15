from os import stat
from mysql.connector import pooling, Error

class Database:
    connection_pool = None
    def __init__(self):
        try:
            db_config = {
                    'user' : 'root',
                    'database' : 'user_database',
                    'host' : 'localhost',
                    'password' : 'Goutham@1005',
                    'port' : 3306,
                    'auth_plugin' : 'mysql_native_password'
                }
            self.connection_pool = pooling.MySQLConnectionPool(
                                    pool_name='new_pool_connection',
                                    pool_size=1,
                                    pool_reset_session=True,
                                    **db_config
                                    )
            # @classmethod
            # def get_connection_from_pool(cls):
            #     return cls.connection_pool.get_connection()

            # @classmethod
            # def return_connection(cls, connection):
            #     cls.connection_pool.add_connection(connection)
        except Exception as e:
            print(e)

class ConnectionFromPool():
    def __init__(self):
        self.connection = None

    def connection_establish():
        database = Database()
        connection = database.connection_pool.get_connection()
        return connection

    def commit_and_return_connection_to_pool(connection):
        print("in commit and return method : ", connection,"\n")
        # connection.commit()
        print("after commit :",connection ,"\n")
        if connection is not None:
            Database.connection_pool.add_connection(connection)

class User:
    def __init__(self, emp_id, emp_name, emp_phoneNumber, emp_email):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_phoneNumber = emp_phoneNumber
        self.emp_email = emp_email


    def save_to_db(self):
        connection = ConnectionFromPool.connection_establish()
        print("in saving method :", connection )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO emp_details(emp_id, emp_name, emp_phoneNumber, emp_email) Values(%s, %s, %s, %s)",
                                                        (self.emp_id, self.emp_name, self.emp_phoneNumber, self.emp_email))
        connection.commit()
        # ConnectionFromPool.commit_and_return_connection_to_pool(connection)

    def load_from_db_by_id(emp_id):
        connection = ConnectionFromPool.connection_establish()
        
        cursor = connection.cursor()
        cursor.execute("select * from emp_details where emp_id = %s", (emp_id,))
        emp_data = cursor.fetchone()
        print(connection)
        # ConnectionFromPool.commit_and_return_connection_to_pool(connection)  by using this line we get the same connection object 3 times. check this out and try to figure out the error 
        return f'emp-details \n {emp_data}'

database = Database()

# save_user_to_db = User(20, 'goutham20', 8682264, 'goutham20@gmail.com')
# save_user_to_db.save_to_db()


user_from_db = User.load_from_db_by_id('2')
print(user_from_db)
user_from_db = User.load_from_db_by_id('3')
print(user_from_db)
user_from_db = User.load_from_db_by_id('5')
print(user_from_db)
user_from_db = User.load_from_db_by_id('1')
print(user_from_db)
user_from_db = User.load_from_db_by_id('6')
print(user_from_db)
user_from_db = User.load_from_db_by_id('8')
print(user_from_db)

# save_user_to_db = User(21, 'goutham21', 86812264, 'goutham21@gmail.com')
# save_user_to_db.save_to_db()







#     if con_obj.is_connected():
        #         print("connected")
                
        #         cursor = con_obj.cursor()
        #         cursor.execute("select * from emp_details;")
        #         records = cursor.fetchall()

        #         for row in records:
        #             print(row)
                    

        # except Error as e:
        #     print(e)
        # finally:
        #     if con_obj.is_connected():
        #         cursor.close()
        #         con_obj.close()
        #         print("closed")