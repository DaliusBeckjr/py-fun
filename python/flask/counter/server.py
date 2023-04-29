from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def root():
    
    # visits = session.get('visits') #retrieve a value from session
    if 'visits' in session:
        print('key exists!')
        session['visits'] += 1 
        
    else:
        print("key does NOT exist")
        session['visits'] = 0
    return render_template('home.html')


@app.route('/destroy_session')
def delete_visits():
    # session.clear()
    session.pop('visits')  #clears a specific key
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True, port=5001)