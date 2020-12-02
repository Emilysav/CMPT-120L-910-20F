from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title='Everything you need to know, and more!')

@app.route('/connect')
def connect():
    return render_template('connect.html', title='Lets connect!')

@app.route('/My Dog')
def dog():
    return render_template('mydog.html', title='Mitzy!')

@app.route('/say something')
def chat():
    return render_template('chat.html', title='Say Something!')

if __name__ == '__main__':
    app.run(debug=True)

