from flask import Flask, request, session, redirect, render_template
import user

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/users')

@app.route('/users')
def show_all_users():
    users= user.User.get_all_users()
    return render_template('user_dashboard.html', all_users=users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')






if __name__ == '__main__':
    app.run(debug=True, port=5001)