# Import the Flask Framework
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('MainPage.html')
    #return 'This site is a work in progress... in the meantime visit my GitHub account <a href="https://github.com/vrk7bp"> here. </a>'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    render_template('ErrorPage.html')
    return 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500