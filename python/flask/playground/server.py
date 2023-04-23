from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template("index.html")


@app.route('/play')
def bluebox(times=3):
    return render_template('home.html', new_times=times)


@app.route('/play/<int:x>')
def second(times, color='maroon'):
    return render_template('home.html', new_times=x, color=color)


@app.route('/play/<int:x>/<color>')
def second(times, color):
    return render_template('home.html', new_times=x, color=color)



if __name__ == '__main__':
    app.run(debug = True, port=5002)