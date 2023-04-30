from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.secret_key = "call me abraham coz we still aint lincoln"

@app.run('/')
def root():
    return render_template('home.html')

@app.run('/result')
def result():
    return render_template('result.html')





if __name__ == "__main__":
    app.run(debug=True, port=5001)