import psycopg2.pool


class Database:
    __connection_pool = None

    @classmethod
    def initialise(cls):
        db_config = {
            'user': 'postgres',
            'password': 'sunny123',
            'database': 'postgre_flask',
            'host': 'localhost'
        }

        cls.__connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 1,
            **db_config
        )
    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()
    
    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()

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
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
    
    # def __repr__(self):
    #     return f'User-Details({self.id}, "{self.name}", {self.phone}, "{self.email}")'


    def save_to_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO user_details(id, name, phone, email) VALUES(%s, %s, %s, %s)", (self.id, self.name, self.phone, self.email))
        
   
    def load_from_db_by_id(id):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM user_details WHERE id=%s", (id,))
                user_data = cursor.fetchone()
                return f'user-details : \n {user_data}'

Database.initialise() #now we can initialise the db whenever we want 
user_from_db = User.load_from_db_by_id('556')
print(user_from_db)

user_from_db = User.load_from_db_by_id('552')
print(user_from_db)

user_from_db = User.load_from_db_by_id('551')
print(user_from_db)

user_from_db = User.load_from_db_by_id('553')
print(user_from_db)