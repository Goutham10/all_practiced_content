from user import User
from database import Database

# my_user = User(556, 'Teja556', 83782837, 'Teja556@gmail.com' )

# # my_user.save_to_db()
Database.initialise() #now we can initialise the db whenever we want 
user_from_db = User.load_from_db_by_id('556')
print(user_from_db)


user_from_db = User.load_from_db_by_id('552')
print(user_from_db)




# print(Database.connection_pool)
# Database.initialise()
# print(Database.connection_pool)