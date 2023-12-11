from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./templates')

# 用于演示的虚拟用户数据，实际中应该使用数据库
users = {'user1': 'password1', 'user2': 'password2'}

# @app.route('/')
# def index():
#     return 'Welcome to the login and signup demo!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return f'Login successful, {username}!'
        else:
            return 'Invalid username or password. Please try again.'

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 实际中应该将新用户数据存储到数据库
        users[username] = password

        return f'Account created for {username}! You can now log in.'

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
