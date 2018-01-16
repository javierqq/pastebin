from flask import Flask
from flask import render_template, request, redirect
from sys import argv
from os.path import exists

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST', 'GET'])
def index():
    languajes = ['Python', 'Ruby', 'JavaScript', 'C']
    if request.method == 'POST':
        if request.form['submit'] == 'Do Something':
            return redirect(url_for(post))
    return render_template('index.html', languajes=languajes)

@app.route('/post', methods=['POST', 'GET'])
def post():
    username = request.form['username']
    languaje = request.form['languaje']
    text = request.form['text']
    return render_template('ex.html',
                            username = username,
                            languaje = languaje,
                            text = text)

if __name__ == "__main__":
    app.run()
