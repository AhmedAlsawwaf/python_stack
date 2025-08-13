from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name': 'Ahmed', 'last_name': 'Alsawaf'},
        {'first_name': 'Mohammed', 'last_name': 'Essa'},
        {'first_name': 'Fatima', 'last_name': 'Hararshah'},
        {'first_name': 'Shahed', 'last_name': 'Fakhory'},
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)