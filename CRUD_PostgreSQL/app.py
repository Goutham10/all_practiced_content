from flask import Flask, redirect, render_template, request, url_for
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add.html")
def add():
    return render_template('add.html')

@app.route("/savedetails", methods=['POST', 'GET'])
def savingDetails():
    if request.method == "POST":
        try:
            id = request.form.get("id")
            name = request.form.get("name")
            phone = request.form.get("phone")
            email = request.form.get("email")

            DB_HOST = "localhost"
            DB_NAME = "postgre_flask"
            DB_USER = "postgres"
            DB_PASS = "sunny123"


            print(id, name, phone, email)
            con = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

            cur = con.cursor()

            cur.execute('INSERT INTO user_details (id, name, phone, email) VALUES (%s, %s, %s, %s)', (id, name, phone, email))

            con.commit()
        except:
            print("incomplete task")
        finally:
            return redirect(url_for("index"))
            

@app.route('/view.html')
def viewRecords():
    DB_HOST = "localhost"
    DB_NAME = "postgre_flask"
    DB_USER = "postgres"
    DB_PASS = "sunny123"

    con = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

    cur = con.cursor()

    cur.execute("SELECT * FROM user_details;")

    list_users = cur.fetchall()
    return render_template("view.html", list_users = list_users)

@app.route("/delete.html", methods=["POST", "GET"])
def delete():
        return render_template('delete.html')

@app.route("/deleteRecord", methods=["POST", "GET"])
def deletingRecord():
    try:
        id = request.form.get("id")
        DB_HOST = "localhost"
        DB_NAME = "postgre_flask"
        DB_USER = "postgres"
        DB_PASS = "sunny123"

        con = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

        cur = con.cursor()

        cur.execute("DELETE FROM user_details WHERE ID={0}".format(id))
        con.commit()
    except:
        print("incomplete task")
    finally:
        return redirect(url_for("index"))

@app.route("/update.html")
def update():
    return render_template("update.html")

@app.route("/edit", methods=["POST", "GET"])
def edit():
    try:
        id = request.form.get("id")
        DB_HOST = "localhost"
        DB_NAME = "postgre_flask"
        DB_USER = "postgres"
        DB_PASS = "sunny123"

        con = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

        cur = con.cursor()

        cur.execute("SELECT * FROM user_details WHERE ID={0}".format(id))
        data = cur.fetchall()
        print(data[0])
        con.commit()
    except:
        print("incomplete task")
    finally:
        return render_template("edit.html", user = data[0])

@app.route("/update/<id>", methods=["POST", "GET"])
def update_user(id):
    if request.method == "POST":
        try:
            name = request.form.get("name")
            phone = request.form.get("phone")
            email = request.form.get("email")

            DB_HOST = "localhost"
            DB_NAME = "postgre_flask"
            DB_USER = "postgres"
            DB_PASS = "sunny123"


            print(id, name, phone, email)
            con = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

            cur = con.cursor()

            cur.execute("UPDATE user_details SET name = %s, phone = %s, email = %s WHERE id = %s", (name, phone, email, id))
            con.commit()
            
        except:
            print("incomplete task")
        finally:
            return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)