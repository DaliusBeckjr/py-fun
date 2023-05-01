from flask import Flask, request, session, redirect, render_template
import user

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/users/dashboard')

@app.route('/users/dashboard')
def show_all_users():
    users= user.User.get_all_users() # import user
    print(users)
    return render_template('user_dashboard.html', all_users=users)







if __name__ == '__main__':
    app.run(debug=True, port=5001)