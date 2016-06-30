from flask import Flask, render_template, request
import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.jinja_env.autoescape = False

order_of_pages = ["/", "/compounds"]

class WebPage():
	def __init__(self, page):
		self.page_number = order_of_pages.index(page)
		self.finalbutton = "Next"
		self.body = ""

	def tidbit(self, name, contents):
		#This is used to add a simple, rounded box with a title and contents
		self.body += render_template('elements.html', element="tidbit",  name=name, contents=contents)

	def form(self, createdform):
		#This is used to add a form
		if self.finalbutton == "Next":
			self.finalbutton = "Submit"
			occurance = "first"
		else:
			occurance = "not first"

		createdform.action = order_of_pages[self.page_number+1]
		self.body += render_template('elements.html', element="form", action=createdform.action, title=createdform.title, body=createdform.body, description=createdform.description, occurance=occurance)

def button_html(title, type="button"):
	return "<button type='" + type + "'>" + title + "</button>"

def make_webpage(createdwebpage):
	if len(order_of_pages) > createdwebpage.page_number+1:
		createdwebpage.body += button_html(createdwebpage.finalbutton, type="submit")
		if createdwebpage.finalbutton == "Submit":
			createdwebpage.body += "</form>"
		createdwebpage.body += order_of_pages[createdwebpage.page_number+1]
	return render_template('index.html', body=createdwebpage.body)

class Create_Form():
	def __init__(self, title, description=""):
		self.title = title
		self.description = description
		self.body = ""

	def input_text(self, caption, name=""):
		if name == "":
			name=caption.lower()
		self.body += "<p>" + caption + """:<br><input name='""" + name + """' type="text" size="30"></p>"""

	def file_upload(self, caption, name=""):
		if name == "":
			name=caption.lower()
		self.body += "<p>"+caption+""":<br><input name='""" + name + """' type="file" size="40"></p>"""

	def textarea(self, caption, name="", rows=4, cols=50, contents=""):
		if name == "":
			name=caption.lower()
		self.body += "<p>" + caption + ":<br><textarea name='""" + name + "' rows='" + str(rows) + "' cols='" + str(cols) + "'>" + contents + "</textarea></p>"

	def radio(self, caption, options, linebreak="no", name=""):
		if name == "":
			name=caption.lower()
		self.body += "<p>"+caption+""": <br>"""
		for option in options:
			self.body += """<input type="radio" name='""" + name + "' value='" + option.lower() + "'> " + option
			if linebreak == "yes":
				self.body += "<br>"
		self.body += "</p>"


@app.route('/')
def start_app():
	website = WebPage("/")

	information = """The type-token ratio (TTR) is an easy-to-calculate measure of functional vocabulary skills. The ratio reflects the diversity of words used by the client during the language sample.
	Templin (1957) reported that normally developing children between the ages of 3 and 8 years have TTRs of .45-.50. A substandard TTR is one indicator of an expressive language delay or disorder.
	TTR is calculated by transcribing a language sample, then counting the total words and the number of different words produced by the client.
	To calculate the TTR, divide the number of different words by the total number of words in the sample."""
	website.tidbit("Type-Token Ratio (TTR)", information)

	new_form = Create_Form("Client Info")
	new_form.input_text("Name")
	new_form.radio("Gender", ["Male", "Female"])
	new_form.input_text("Birthdate (MM/DD/YYYY)", "birthdate")
	website.form(new_form)

	new_form = Create_Form("Language Sample")
	new_form.textarea("Copy and paste the language sample here", "languagesample")
	new_form.file_upload("Or select a text file from your computer", "languagesample")
	new_form.input_text("Date of Elicitation (MM/DD/YYYY)","date")
	website.form(new_form)

	return make_webpage(website)

@app.route('/compounds', methods=['GET'])
def choose_compounds():
	return "Welcome to the compounds page! "+request.form['gender']

@app.route('/shutdown')
def shutdown():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()
	return 'Server shutting down...'

if __name__ == '__main__':
	app.run(threaded=True, debug=True)