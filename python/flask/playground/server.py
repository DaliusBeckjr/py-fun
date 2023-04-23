from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/play/<int:times>')
def repeat(times):
    return render_template('home.html', new_times=times)





if __name__ == '__main__':
    app.run(debug = True, port=5002)