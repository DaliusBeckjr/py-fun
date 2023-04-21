from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello world!"

@app.route('/say/<name>')
def say_name(name):
    return render_template('say_name.html', this_name = name)


@app.route('/home_page')
def home():
    return render_template('home.html', this_name)


@app.route('/say/<name>/<int:times>')
def repeat(name, times):
    return render_template(template_name_or_list)






if __name__ == "__main__":
    app.run(debug=true, port=5001) # for new mac users put 'port=5001' cos of s