from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Start playing'
@app.route('/play')
def play():
    return render_template('index.html', times = 3)
@app.route('/play/<int:x>')
def play_repeat(x):
    return render_template('index.html',times=x)
@app.route('/play/<int:x>/<color_background>')
def play_repeat_with_color(x,color_background):
    return render_template('index.html',times=x,color=color_background)

if __name__ == "__main__":
    app.run(debug=True)