from flask import Flask, render_template
import logging


app=Flask(__name__)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/')
@app.route('/home')
def homepage():
    logging.info("someone's on the site!")
    return render_template('homepage.html', title='Home Page')

@app.route('/about')
def about():
    logging.info("view on about me")
    return render_template('about.html', title='Everything you need to know, and more!')

@app.route('/connect')
def connect():
    logging.info("if someone adds you, don't say you don't know why")
    return render_template('connect.html', title='Lets connect!')

@app.route('/My Dog')
def dog():
    logging.info("someone just learned about mitzy")
    return render_template('mydog.html', title='Mitzy!')

@app.errorhandler(404)
def not_found(e):
    logging.error("encountered a 404pnf error")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

