# Import the Flask Framework
from flask import Flask, render_template, redirect, request
from google.appengine.api import mail

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('MainPage.html')

@app.route('/aboutme')
def aboutMe():
	return render_template('AboutMe.html')

@app.route('/testing')
def testing():
	return render_template('MainPageSeptember6th2014.html')

@app.route('/aboutsite')
def aboutSite():
	return render_template('AboutSite.html')

@app.route('/timduncan')
def timDuncan():
	return render_template('TimDuncan.html')

@app.route('/timduncansignup', methods=['POST'])
def timDuncanSignUp():
	text = request.form['text']
	if(text.count("@") != 0):
		mail.send_mail(sender="Tim Duncan <venkata.gautam@gmail.com>",
              to="Gautam <gautamkwebsite@gmail.com>",
              subject="Add someone to Tim Duncan List",
              body=text)
		return redirect("http://www.gautamk.us", code=302)
	return redirect("http://www.gautamk.us/timduncan", code=302)

@app.route('/timduncanquit', methods=['POST'])
def timDuncanQuit():
	text = request.form['textQuit']
	if(text.count("@") != 0):
		mail.send_mail(sender="Tim Duncan <venkata.gautam@gmail.com>",
              to="Gautam <gautamkwebsite@gmail.com>",
              subject="Unsubscribe someone from Tim Duncan List",
              body=text)
		return redirect("http://www.gautamk.us", code=302)
	return redirect("http://www.gautamk.us/timduncan", code=302)

@app.route('/projects')
def projects():
	return render_template('Projects.html')

@app.route('/pubs')
def publications():
	return render_template('Publications.html')

@app.route('/tracking')
def tracker():
	return render_template('tracker.html')

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

@app.route('/fieabstract')
def fieabstract():
	return redirect("https://s3.amazonaws.com/GautamResume/FIEAbstract.pdf", code=302)

@app.route('/fiepaper')
def fiepaper():
	return redirect("https://s3.amazonaws.com/GautamResume/FIEPaper.pdf", code=302)

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page."""
    return render_template('ErrorPage.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    """Custom 500 Page."""
    return render_template('500Error.html'), 500