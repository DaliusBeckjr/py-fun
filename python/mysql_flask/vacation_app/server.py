from flask import Flask, redirect, session, render_template
import user # this one takes the whole page of information
# from user import user # 

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/users/dashboard')

@app.route('/users/dashboard')
def all_users():
    users= user.User.get_all_users() # import user
    print(users)
    return render_template('user_dashboard.html', all_users= users)


if __name__ == "__main__":
    app.run(debug=True, port=5001)