from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      userName = request.form.get('name')
      userAge = request.form.get('age')
      print("user details by using post method : ")
      print("user name is "+userName + " and age is "+userAge)
      return redirect(url_for('postMethodCall'))
      
   elif request.method == 'GET':
      userName = request.form.get('name')
      userAge = request.form.get('age')
      print("user details by using get method : ")
      print("user name is "+str(userName) + "and age is "+str(userAge))
      # return redirect(url_for('getMethodCall'))
   return render_template('home.html')


@app.route('/postMethodCall')
def postMethodCall():
   return render_template('postOperation.html') 

@app.route('/getMethodCall')
def getMethodCall():
   return render_template('getOperation.html')




if __name__ == '__main__':
   app.run(debug = True)