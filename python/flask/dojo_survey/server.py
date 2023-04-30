from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'call me abraham coz we still aint lincoln'

# our index route will handle rendering our form
@app.route('/')
def root():
    return render_template("home.html")

@app.route('/users/results', methods=['POST'])
def create_user():
    print('got post info!')
    print(request.form)
    
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    return redirect ('/users/show_results')





@app.route('/users/show_results')
def show_results():
    return render_template('show_results.html')




if __name__ == "__main__":
    app.run(debug=True, port=8801) #if localhost doesn't work try host='127.0.0.1'

