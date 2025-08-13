from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/lists')
def render_lists():
    student_info =[
        {'name' :'Ahmed', 'age':18},
        {'name' :'Ali', 'age':28},
        {'name' :'Ameer', 'age':38},
        {'name' :'Moayad', 'age':48},
    ]
    return render_template('lists.html', random_numbers = [3,1,5],students=student_info)

if __name__ == '__main__':
    app.run(debug = True)