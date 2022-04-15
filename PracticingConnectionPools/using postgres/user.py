from database import ConnectionFromPool

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