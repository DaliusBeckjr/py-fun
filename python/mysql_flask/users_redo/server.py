from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/users')

@app.route('/users')
def user():
    user=user.User.get_all_users()
    return render_template("show_user.html", users=user)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create')
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')








if __name__ == '__main__':
    app.run(debug=True, port=8801)