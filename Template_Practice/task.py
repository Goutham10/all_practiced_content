import psycopg2
DB_HOST = "localhost"
DB_NAME = "postgre_flask"
DB_USER = "postgres"
DB_PASS = "sunny123"



con = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

cur = con.cursor()
# print(con)

cur.execute('INSERT INTO employee (first_name, last_name, salary) VALUES (%s, %s, %s)', ("sirisha","vimula",35000.00))
print("success")
con.commit()