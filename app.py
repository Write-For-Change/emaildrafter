from flask import Flask, render_template, flash, jsonify, request, url_for
from emails import draftEmails
from urllib import parse
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def landing():
	if request.method == 'GET':
		return render_template('landing.html')
	else:
		name = request.form['name']
		postcode = request.form['postcode']
		postcode = postcode.replace(" ", "")
		emails = draftEmails(name, postcode)
		a = [{'email': (e.email), 'subject_coded': parse.quote(e.subject), 'body_coded': parse.quote(e.body), 'subject': (e.subject), 'body': (e.body)} for e in emails]
		# return jsonify(a)
		return render_template('emails.html', emails=a)