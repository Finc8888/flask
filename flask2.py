from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
	return app.send_static_file('flask2.html')
@app.route('/echo/<thing>')
def echo(thing):
	"""
	Аргумент thing = thing означает, что для передачи переменной с именем thing
	в шаблон эта переменная содержит значение строки thing .
	"""
	return render_template('flask2.html', thing=thing)
app.run(port=9999, debug=True)
