<h1>Python Password Generator Web Application</h1>

<h3>Description</h3>
<p><strong>Python Password Generator</strong> is a Flask-based web application designed to create secure, customizable passwords based on a user-specified length. Users can generate passwords using letters, numbers, and special characters, providing an extra layer of security.</p>

<h3>Prerequisites</h3>
<p>To run this project, make sure you have Python and Flask installed on your system.</p>
<ul>
    <li><strong>Install Flask</strong>: Run the following command to install Flask:
        <pre><code>pip install Flask</code></pre>
    </li>
</ul>

<h3>Installation</h3>
<ol>
    <li><strong>Step 1: Clone the Repository</strong>
        <ul>
            <li>Clone the repository to your local machine:</li>
            <pre><code>git clone https://github.com/yourusername/Password-Generator.git</code></pre>
            <li>Navigate into the project directory:</li>
            <pre><code>cd Password-Generator</code></pre>
        </ul>
    </li>
    <li><strong>Step 2: Start the Flask Server</strong>
        <ul>
            <li>Start the Flask server by running:</li>
            <pre><code>python app.py</code></pre>
            <li>Once the server is running, open your browser and navigate to <a href="http://127.0.0.1:5000/" target="_blank">http://127.0.0.1:5000/</a>.</li>
        </ul>
    </li>
</ol>

<h3>Features</h3>
<ul>
    <li><strong>Customizable Password Length</strong>: Allows users to specify the desired length for a generated password.</li>
    <li><strong>Secure Password Generation</strong>: Generates passwords using a mix of letters, numbers, and symbols to enhance password strength.</li>
    <li><strong>Real-Time Interaction</strong>: Responds to user input instantly, generating a password upon request.</li>
    <li><strong>JSON Data Transfer</strong>: Returns the generated password in JSON format, making it easy to integrate with other applications.</li>
</ul>

<h3>Code Overview</h3>

<h4>Flask Backend</h4>
<p>The Flask backend, defined in <code>app.py</code>, sets up the server and handles the logic for generating passwords.</p>

<pre><code>from flask import Flask, render_template, request, jsonify
import string
import random

app = Flask(__name__)

def generate_password(length):
    # Generates a secure password with letters, numbers, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/")
def index():
    # Renders the main HTML page
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Retrieves password length from the form and generates a password
    length = int(request.form.get('length'))
    password = generate_password(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
</code></pre>

<p><strong>Explanation:</strong></p>
<ul>
    <li><strong>generate_password</strong> function: Randomly generates a password of specified length using letters, digits, and punctuation characters.</li>
    <li><strong>Routes</strong>:
        <ul>
            <li><code>/</code>: Displays the main page.</li>
            <li><code>/generate</code>: Processes the user’s input and returns a JSON response with the generated password.</li>
        </ul>
    </li>
</ul>

<h4>HTML Frontend</h4>
<p>The <code>index.html</code> file provides a form where users can enter their desired password length and submit to generate a password.</p>

<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Password Generator&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Password Generator&lt;/h1&gt;
    &lt;form id="password-form"&gt;
        &lt;label for="length"&gt;Password Length:&lt;/label&gt;
        &lt;input type="number" id="length" name="length" required&gt;
        &lt;button type="submit"&gt;Generate Password&lt;/button&gt;
    &lt;/form&gt;
    &lt;p id="result"&gt;&lt;/p&gt;

    &lt;script&gt;
        document.getElementById('password-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const length = document.getElementById('length').value;

            fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ length: length }),
            })
            .then(response =&gt; response.json())
            .then(data =&gt; {
                document.getElementById('result').textContent = `Generated Password: ${data.password}`;
            })
            .catch(error =&gt; console.error('Error:', error));
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>

---

<h3>Usage</h3>
<p>To generate a password, make a <code>POST</code> request to the <code>/generate</code> endpoint with a <code>length</code> parameter.</p>

<h4>Example Request</h4>
<pre><code>curl -X POST -d "length=12" http://127.0.0.1:5000/generate</code></pre>

<h4>Example Response</h4>
<pre><code>{
  "password": "A@3g9#!aB$6f"
}
</code></pre>
<p>This example generates a 12-character password with a mix of letters, numbers, and symbols.</p>

---

<h3>What I Learned</h3>
<ul>
    <li><strong>Flask Basics</strong>: Learned to initialize a Flask server, define routes, and manage requests.</li>
    <li><strong>Template Rendering</strong>: Used <code>render_template</code> to load HTML templates.</li>
    <li><strong>User Input Handling</strong>: Captured user input with <code>request.form.get()</code>.</li>
    <li><strong>JSON Formatting</strong>: Used <code>jsonify</code> to send the password in JSON format.</li>
</ul>

<h3>Future Plans</h3>
<ul>
    <li>Additional Customization: Add options to include or exclude specific types of characters.</li>
    <li>Enhanced Styling: Improve the layout and design for a better user experience.</li>
    <li>Password Management: Implement options to save and manage generated passwords securely.</li>
</ul>

<h3>Support & Feedback</h3>
<p>If you found this project helpful, please consider leaving feedback to support my growth as a Python and Flask developer. Suggestions are always welcome!</p>

<p><a href="https://x.com/kelvinintech" target="_blank" style="text-decoration: none;">
   <button style="background-color: #1DA1F2; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px;">
       Follow Me on X
   </button>
</a></p>
