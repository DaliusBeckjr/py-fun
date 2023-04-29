from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.secret_key = "keep it a secret"

@app.run('/')
def root():
    return render_template('home.html')







if __name__ == "__main__":
    app.run(debug=True, port=5001)