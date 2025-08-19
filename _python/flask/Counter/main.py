from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)  
app.secret_key ='lmD49}+*dCK#/<qEi"y3c~*A9*[9eeAr4hJz%NXy}kIy~BT|sr=Vq"^vg1on8Y]'

@app.route('/')
def debugCounter():
    session['visit_count'] = session.get('visit_count', 0) + 1
    return render_template('index.html',count= session['visit_count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment')
def increment():
    session['visit_count'] = session.get('visit_count', 0) + 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)   