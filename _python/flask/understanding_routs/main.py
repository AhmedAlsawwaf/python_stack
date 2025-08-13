from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World !'

@app.route('/champion')
def champion():
    return 'Champion!'

@app.route('/say/<name>')
def greet(name):
    formatted_name = name.capitalize()
    return f'Hi {formatted_name} .'

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num,word):
    return ' '.join([word]*num)

if __name__ == '__main__':
    app.run(debug=True)