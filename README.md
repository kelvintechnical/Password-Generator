<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Generator Web Application README</title>
</head>
<body>
    <h1>Python Password Generator Web Application</h1>

    <h2>Description</h2>
    <p>The Python Password Generator is a Flask-based web application designed to create secure, customizable passwords based on a user-specified length. Users can easily generate passwords using letters, numbers, and special characters, offering them an extra layer of security for their accounts. This project helped reinforce my understanding of Python, Flask, and web development concepts.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Customizable Password Length</strong>: Allows users to specify their desired password length.</li>
        <li><strong>Secure Password Generation</strong>: Creates passwords using a mix of letters, numbers, and symbols for optimal security.</li>
        <li><strong>Real-Time Interaction</strong>: Users receive a password instantly upon submitting their request.</li>
        <li><strong>JSON Data Transfer</strong>: Returns the generated password in JSON format, ensuring data is ready for frontend use.</li>
    </ul>

    <h2>What I Learned</h2>
    <p>Working on this project provided me with hands-on experience in Python web development and Flask. Key takeaways include:</p>
    <ul>
        <li><strong>Flask Basics</strong>: Learned how to set up a Flask application, create routes, and handle user requests.</li>
        <li><strong>Route Management</strong>: Used <code>@app.route</code> to define specific application behavior based on URL routes, handling multiple endpoints.</li>
        <li><strong>HTML and Template Rendering</strong>: Leveraged <code>render_template</code> to connect Python code with HTML templates for a responsive interface.</li>
        <li><strong>Handling User Input with Flask</strong>: Captured user input using <code>request.form.get()</code>, enabling real-time input processing and password customization.</li>
        <li><strong>JSON Formatting</strong>: Implemented <code>jsonify</code> to return data in JSON format, making the password easily accessible on the frontend.</li>
        <li><strong>Randomized Password Generation</strong>: Developed a function using <code>string</code> and <code>random</code> libraries to generate complex passwords by randomly selecting characters from a secure character pool.</li>
    </ul>

    <h2>How to Use</h2>

    <h3>Installation:</h3>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/yourusername/Password-Generator.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd Password-Generator</code></pre>
        </li>
        <li>Install Flask:
            <pre><code>pip install Flask</code></pre>
        </li>
        <li>Run the application:
            <pre><code>python app.py</code></pre>
        </li>
        <li>Open your browser and visit <code>http://127.0.0.1:5000/</code> to use the password generator.</li>
    </ol>

    <h3>Customization:</h3>
    <p>Specify the password length in the input field on the main page. Submit your request, and the generated password will be displayed instantly.</p>

    <h2>Future Plans</h2>
    <p>As I continue building my Python and Flask skills, I plan to enhance this project by:</p>
    <ul>
        <li>Adding options for more specific character selections (e.g., exclude special characters).</li>
        <li>Creating a user-friendly interface with improved styling.</li>
        <li>Implementing security measures to store and manage passwords securely.</li>
    </ul>

    <h2>Support & Feedback</h2>
    <p>If you found this project helpful, please like, comment, or give feedback to support my growth as a Python and Flask developer. Any suggestions are greatly appreciated as I continue learning!</p>
</body>
</html>
