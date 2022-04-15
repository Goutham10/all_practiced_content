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
