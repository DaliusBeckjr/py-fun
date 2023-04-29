from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/count')
def root():
    return render_template('home.html')






if __name__ == "__main__":
    app.run(debug=True, port=5001)