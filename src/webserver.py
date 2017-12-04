from flask import Flask, render_template, send_from_directory
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

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('templates/js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('templates/css', path)

@app.route('/docs/<path:path>')
def send_docs(path):
	return send_from_directory('docs', path)

@app.route('/img/<path:path>')
def send_img(path):
	return send_from_directory('img', path)


def main():
	app.run(host='0.0.0.0', port=80, threaded=True, debug=True)

if __name__ == '__main__':
	main()