from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello world"
# once running the virtualenv in term 'pipenv shell'
#search localhost:('port number here')

@app.route('/say/<name>')
def say_name(name):
    return render_template('say_name.html', this_name=name.upper())
    # return f"my name is {name}"

@app.route('/homepage')
def home():
    return render_template('home.html')






# has to be at the bottom
if __name__ == '__main__':
    app.run(debug=True, port=5001)