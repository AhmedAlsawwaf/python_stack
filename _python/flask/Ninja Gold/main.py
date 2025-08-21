from flask import Flask,render_template,redirect,session,request
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = 'lmD49}+*dCK#/<qEi"y3c~*A9*[9eeAr4hJz%NXy}kIy~BT|sr=Vq"^vg1on8Y]'  

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html',gold=session['gold'],activities=session['activities'] )

@app.route('/process_money',methods=['POST'])
def process_money():
    building = request.form['building']
    if building == 'farm':
        gold = random.randint(10,20) 
        profit = True
    elif building =='cave':
        gold = random.randint(5,10) 
        profit = True
    elif building =='house':
        gold = random.randint(2,5) 
        profit = True
    elif building =='casino':
        gold = random.randint(0,50) 
        profit = random.choice([False,True])
    
    if profit:
        session['gold'] += gold
        message = f'You earn {gold} golds from the {building}   '+'({:%Y/%m/%d %I:%M %p})'.format(datetime.now())

    else:
        session['gold'] -= gold
        message = f'You lose {gold} golds from the {building}   '+'({:%Y/%m/%d %I:%M %p})'.format(datetime.now())
    session['activities'].append({
        'message': message,
        'profit': profit})

    return redirect('/')

@app.route('/clear', methods=['POST'] )
def clear():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)