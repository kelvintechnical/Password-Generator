# Python Password Generator Web Application

## Description
The Python Password Generator is a Flask-based web application designed to create secure, customizable passwords based on a user-specified length. Users can easily generate passwords using letters, numbers, and special characters, offering an extra layer of security.

---

## Prerequisites
To run this project, ensure that Python and Flask are installed on your system. You can install Flask by running:

```bash
pip install Flask


Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/Password-Generator.git
cd Password-Generator


Running the Application
Start the Flask server by running the following command:

bash
Copy code
python app.py
Once the server is running, open your browser and navigate to http://127.0.0.1:5000/.

Features
Customizable Password Length: Users can specify the desired password length.
Secure Password Generation: Generates passwords using a mix of letters, numbers, and symbols for enhanced security.
Real-Time Interaction: Users receive a password immediately upon submitting their request.
JSON Data Transfer: Returns the generated password in JSON format, making it ready for frontend use.
Code Overview
This project consists of two main components: the Flask backend and an HTML frontend.

Flask Backend
app.py: Sets up the Flask server and defines routes to handle user requests.

generate_password function: Generates a secure password by selecting characters from letters, digits, and punctuation symbols.

python
Copy code
from flask import Flask, render_template, request, jsonify
import string
import random

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form.get('length'))
    password = generate_password(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
