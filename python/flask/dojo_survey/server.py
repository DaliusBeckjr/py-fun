from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'call me abraham coz we still aint lincoln'

# our index route will handle rendering our form
@app.route('/')
def root():
    return render_template("home.html")






if __name__ == "__main__":
    app.run(debug=True, port=5001)

