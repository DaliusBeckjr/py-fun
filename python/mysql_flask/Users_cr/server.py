from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html')







if __name__ == '__main__':
    app.run(debug=True, port=5001)