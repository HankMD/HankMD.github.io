from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('about.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/work')
def work():
	return render_template('work.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/docs/<pdf_file>')
def get_pdf(pdf_file):
    return send_file(
		'../docs/' + pdf_file,  # file path or file-like object
		'application/pdf',
		as_attachment=False,
		attachment_filename=pdf_file
	)



def main():
	app.run(host='0.0.0.0', port=80, threaded=True, debug=True)

if __name__ == '__main__':
	main()