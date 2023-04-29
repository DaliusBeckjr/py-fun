from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# our index route will handle rendering our form
@app.route('/')
def root():
    return render_template("home.html")

@app.route('/users/create', methods=['POST'])
def create_user():
    print("we got post info!")
    print(request.form)
    print(request.form['first_name'])
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    # should print the first_name value after ImmutableMultiDict
    # return render_template('show_user', user=request.form)
    return redirect('users/show_user')


@app.route('/users/test', methods=['POST']) 
def user_test():
    return f"sensational {request.form['user_name']}"


@app.route('users/show_user')
def show_user():
    return render_template('show_user.html', users=request.form)




if __name__ == "__main__":
    app.run(debug=True, port=5001)

