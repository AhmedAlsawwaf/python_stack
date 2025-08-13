from flask import Flask,render_template
app = Flask(__name__)


@app.route('/<int:rows>/<int:columns>')
def custom_rows_columns(rows, columns):
    return render_template('index.html', rows=rows, columns=columns)

@app.route('/<int:rows>')
def custom_rows(rows):
    return render_template('index.html', rows=rows, columns=8)

@app.route('/')
def index():
    return render_template('index.html', rows=8, columns=8)

if __name__ =='__main__':
    app.run(debug=True)