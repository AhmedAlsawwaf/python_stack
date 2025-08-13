from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        form_data = {
            'name': request.form['name'],
            'gender': request.form['gender'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form.get('comment', '')
        }
        
        return render_template('index.html',
                            name_from_template=form_data['name'],
                            gender_from_template=form_data['gender'],
                            location_from_template=form_data['location'],
                            language_from_template=form_data['language'],
                            comment_from_template=form_data['comment'],
                            show_results=True)
    else:
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)