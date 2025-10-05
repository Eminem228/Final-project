from flask import Flask, request, jsonify, render_template_string, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='templates', static_url_path='', template_folder='templates')

users = []

# Главная страница с формой регистрации
@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registration</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
            }
            .form-container {
                background: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 300px;
            }
            h1 {
                text-align: center;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
            input {
                width: 100%;
                padding: 8px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                width: 100%;
                padding: 10px;
                border: none;
                border-radius: 4px;
                background-color: #007bff;
                color: #fff;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            .link {
                text-align: center;
                margin-top: 10px;
            }
            .link a {
                color: #007bff;
                text-decoration: none;
            }
            .link a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>Register</h1>
            <form action="/register" method="POST">
                <label for="username">Name:</label>
                <input type="text" id="username" name="username" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>

                <button type="submit">Register</button>
            </form>
            <div class="link">
                <p>Already have an account? <a href="/login_page">Login here</a></p>
            </div>
        </div>
    </body>
    </html>
    ''')

# Страница входа
@app.route('/login_page')
def login_page():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
            }
            .form-container {
                background: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 300px;
            }
            h1 {
                text-align: center;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
            input {
                width: 100%;
                padding: 8px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                width: 100%;
                padding: 10px;
                border: none;
                border-radius: 4px;
                background-color: #28a745;
                color: #fff;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background-color: #218838;
            }
            .link {
                text-align: center;
                margin-top: 10px;
            }
            .link a {
                color: #28a745;
                text-decoration: none;
            }
            .link a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>Login</h1>
            <form action="/login" method="POST">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>

                <button type="submit">Login</button>
            </form>
            <div class="link">
                <p>Don't have an account? <a href="/">Register here</a></p>
            </div>
        </div>
    </body>
    </html>
    ''')

# Регистрируем нового пользователя
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Проверка на существование пользователя с таким же email
    if any(user['email'] == email for user in users):
        return 'A user with that email already exists!', 400

    # Хешируем пароль
    hashed_password = generate_password_hash(password)

    # Добавляем пользователя в память
    users.append({
        'username': username,
        'email': email,
        'password': hashed_password
    })

    return f'User {username} has been registered successfully! <a href="/login_page">Login here</a>'

# Вход пользователя
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Ищем пользователя по email
    user = next((u for u in users if u['email'] == email), None)
    if user and check_password_hash(user['password'], password):
        return f'Welcome back, {user["username"]}!'
    else:
        return 'Invalid email or password!', 401

# Список зарегистрированных пользователей 
@app.route('/users')
def show_users():
    users_safe = [{'username': u['username'], 'email': u['email']} for u in users]
    return jsonify(users_safe)

if __name__ == '__main__':
    app.run(debug=True)
