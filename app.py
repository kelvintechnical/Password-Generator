from flask import Flask, render_template, request, jsonify
import string
import random

#flask creates the app
#render_template loads the HTML page
#requests allows us to get data from the user
#jsonify sends data back to the user in a format they can use
#route in Flask and webdev refers to a specific url to your applicaiton
#       determines how the application behaves when auser visits a certain URL


app = Flask(__name__)
#represents the name of the current module
#helps Flask know where to look for resources

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range (length))
    return password


#app.route('/') is about defining what happens when someone visits a specific url in the app

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form.get('length'))
    password = generate_password(length)
    return jsonify ({'password': password})

if __name__ == '__main__':
    app.run(debug=True)