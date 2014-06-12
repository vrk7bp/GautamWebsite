# Import the Flask Framework
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('MainPage.html')

@app.route('/aboutme')
def aboutMe():
	return render_template('AboutMe.html')

@app.route('/aboutsite')
def aboutSite():
	return render_template('AboutSite.html')

@app.route('/projects')
def projects():
	return render_template('Projects.html')

@app.route('/pubs')
def publications():
	return render_template('Publications.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/nasa')
def nasa():
	return redirect("http://www.seas.virginia.edu/pubs/spectra/pdfs/nasapartnerships.pdf", code=302)

@app.route('/resume')
def resume():
	return redirect("https://s3.amazonaws.com/GautamResume/GautamKanumuruResume.pdf", code=302)

@app.route('/uvradiationabstract')
def uvabstract():
	return redirect("https://s3.amazonaws.com/GautamResume/UVAbstract.pdf", code=302)

@app.route('/uvradiationpaper')
def uvpaper():
	return redirect("https://s3.amazonaws.com/GautamResume/UVPaper.pdf", code=302)

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page."""
    return render_template('ErrorPage.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    """Custom 500 Page."""
    return render_template('500Error.html'), 500