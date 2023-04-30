from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def root():
    if "visits" not in session:
        session["visits"] = 0
        print("key does NOT exist")
    else:
        session["visits"] +=1
        print('key exists!')
    return render_template('home.html')

@app.route('/reset')
def reset():
    session.pop("visits", None) #clears a specific value
    return redirect('/')
    


if __name__ == "__main__":
    app.run(debug=True, port=5001)