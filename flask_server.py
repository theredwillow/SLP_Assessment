from flask import Flask, render_template, request
import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.jinja_env.autoescape = False

order_of_pages = ["/"]

class WebPage():
	def __init__(self):
		self.body = ""

	def tidbit(self, name, contents):
		#This is used to add a simple, rounded box with a title and contents
		self.body += render_template('elements.html', element="tidbit",  name=name, contents=contents)

	def form(self, createdform):
		#This is used to add a form
		if createdform.description == "":
			self.body += render_template('elements.html', element="form", title=createdform.title, body=createdform.body)
		else:
			self.body += render_template('elements.html', element="form", title=createdform.title, body=createdform.body, description=createdform.description)

def make_webpage(createdwebpage):
	action="Poop"
	if action == "":
		createdwebpage.body += "Next"
	else:
		createdwebpage.body += "Submit" 
	return render_template('index.html', body=createdwebpage.body)

class Create_Form():
	def __init__(self, title, description=""):
		self.title = title
		self.description = description
		self.body = ""

	def input_text(self, caption):
		self.body += "<p>"+caption+""":<br><input type="text" name="textline" size="30"></p>"""

	def file_upload(self, caption):
		self.body += "<p>"+caption+""":<br><input type="file" name="datafile" size="40"></p>"""

	def textarea(self, caption, rows=4, cols=50, contents=""):
		self.body += "<p>"+caption+":<br><textarea rows='" + str(rows) + "' cols='" + str(cols) + "'>" + contents + "</textarea></p>"

	def radio(self, caption, options, linebreak="no"):
		self.body += "<p>"+caption+""": <br>"""
		for option in options:
			self.body += """<input type="radio" name='""" + caption + "' value='" + option + "'> " + option
			if linebreak == "yes":
				self.body += "<br>"
		self.body += "</p>"


@app.route('/')
def start_app():
	website = WebPage()

	information = """The type-token ratio (TTR) is an easy-to-calculate measure of functional vocabulary skills. The ratio reflects the diversity of words used by the client during the language sample.
	Templin (1957) reported that normally developing children between the ages of 3 and 8 years have TTRs of .45-.50. A substandard TTR is one indicator of an expressive language delay or disorder.
	TTR is calculated by transcribing a language sample, then counting the total words and the number of different words produced by the client.
	To calculate the TTR, divide the number of different words by the total number of words in the sample."""

	website.tidbit("Type-Token Ratio (TTR)", information)

	new_form = Create_Form("Language Sample")
	new_form.textarea("Copy and paste the language sample here")
	new_form.file_upload("Or select a text file from your computer")
	new_form.input_text("Date of Elicitation (MM/DD/YYYY)")
	website.form(new_form)

	new_form = Create_Form("Client Info")
	new_form.input_text("Name")
	new_form.radio("Gender", ["Male", "Female"])
	new_form.input_text("Birthday (MM/DD/YYYY)")
	website.form(new_form)

	return make_webpage(website)

@app.route('/shutdown')
def shutdown():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()
	return 'Server shutting down...'

if __name__ == '__main__':
	app.run(threaded=True, debug=True)