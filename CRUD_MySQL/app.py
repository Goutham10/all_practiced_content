from flask import Flask, redirect, render_template, request, url_for
import mysql.connector

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "user_database"
DB_USER = "root"
DB_PASS = "Goutham@1005"

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


            print(id, name, phone, email)
            con = mysql.connector.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

            cur = con.cursor()

            cur.execute('INSERT INTO user_details (id, name, phone, email) VALUES (%s, %s, %s, %s)', (id, name, phone, email))

            con.commit()
        except:
            print("incomplete task")
        finally:
            return redirect(url_for("index"))
            

@app.route('/view.html')
def viewRecords():
    

    con = mysql.connector.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

    cur = con.cursor()

    cur.execute("SELECT * FROM user_details;")

    list_users = cur.fetchall()
    print(list_users)
    return render_template("view.html", list_users = list_users)

@app.route("/delete.html", methods=["POST", "GET"])
def delete():
        return render_template('delete.html')

@app.route("/deleteRecord", methods=["POST", "GET"])
def deletingRecord():
    try:
        id = request.form.get("id")
        
        con = mysql.connector.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

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
       

        con = mysql.connector.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

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

            print(id, name, phone, email)
            con = mysql.connector.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

            cur = con.cursor()

            cur.execute("UPDATE user_details SET name = %s, phone = %s, email = %s WHERE id = %s", (name, phone, email, id))
            con.commit()
            
        except:
            print("incomplete task")
        finally:
            return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)