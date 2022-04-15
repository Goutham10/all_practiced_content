import mysql.connector.pooling

class Database:
    connection_pool = None

    @classmethod
    def initialise(cls):
        db_config = {
            'user' : 'root',
            'database' : 'user_database',
            'host' : 'localhost',
            'password' : 'Goutham@1005',
            'port' : 3306
        }

        cls.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name = "new_pool",
            pool_size = 10,
            auth_plugin='mysql_native_password',
            **db_config)

    @classmethod
    def get_connection(cls):
        return cls.connection_pool.get_connection()
    
    @classmethod
    def return_connection(cls,connection):
        cls.connection_pool.add_connection(connection)

    @classmethod
    def close_all_connections(cls):
        cls.connection_pool.closeall()

    

class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = Database.get_connection()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        Database.return_connection(self.connection)


class User:
    def __init__(self, emp_id, emp_name, emp_phoneNumber, emp_email):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_phoneNumber = emp_phoneNumber
        self.emp_email = emp_email
    
    # def __repr__(self):
    #     return f'User-Details({self.id}, "{self.name}", {self.phone}, "{self.email}")'


    def save_to_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO emp_details(emp_id, emp_name, emp_phoneNumber, emp_email) VALUES(%s, %s, %s, %s)", (self.emp_id, self.emp_name, self.emp_phoneNumber, self.emp_email))
        
   
    def load_from_db_by_id(emp_id):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM emp_details WHERE emp_id=%s", (emp_id,))
                user_data = cursor.fetchone()
                return f'user-details : \n {user_data}'

Database.initialise() #now we can initialise the db whenever we want 
user_from_db = User.load_from_db_by_id('1')
print(user_from_db)

user_from_db = User.load_from_db_by_id('2')
print(user_from_db)

user_from_db = User.load_from_db_by_id('3')
print(user_from_db)

user_from_db = User.load_from_db_by_id('4')
print(user_from_db)