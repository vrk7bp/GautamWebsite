# Import the Flask Framework
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('MainPage2.html')
    #return 'This site is a work in progress... in the meantime visit my GitHub account <a href="https://github.com/vrk7bp"> here. </a>'


@app.route('/main')
def testing():
	return render_template('MainPage.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/nasa')
def nasa():
	return redirect("http://www.seas.virginia.edu/pubs/spectra/pdfs/nasapartnerships.pdf", code=302)

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page."""
    return render_template('ErrorPage.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    """Custom 500 Page."""
    return render_template('500Error.html'), 500