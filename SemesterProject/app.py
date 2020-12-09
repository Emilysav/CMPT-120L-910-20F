from flask import Flask
from Flask import render_template
from Flask import logging

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

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

