# app.py
from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'lmD49}+*dCK#/<qEi"y3c~*A9*[9eeAr4hJz%NXy}kIy~BT|sr=Vq"^vg1on8Y]'  

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['game_over'] = False
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if session.get('game_over'):
        return redirect('/')
    
    guess = int(request.form['guess'])
    session['attempts'] += 1
    secret_number = session['number']
    
    if guess == secret_number:
        session['game_over'] = True
        result = 'correct'
        message = f'Congratulations! You guessed it in {session["attempts"]} attempts!'
    elif guess < secret_number:
        result = 'low'
        message = 'Too Low!'
    else:
        result = 'high'
        message = 'Too High!'
    
    return render_template('index.html', result=result, message=message)

@app.route('/play_again', methods=['POST'])
def play_again():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)