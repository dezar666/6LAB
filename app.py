from flask import Flask, request, render_template
from jinja2 import Template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    name, age, proffesion = 'Anton', 21, '3D-Artist'
    template_context = dict(name=name, age=age, proffesion=proffesion)
    return render_template('index.html', **template_context)


@app.route('/search/')
def search():
    return render_template('search.html')


@app.route('/result/')
def result():
    return 'There will be result'

@app.route('/request/')
def request():
    return 'This is request page'


if __name__ == '__main__':
    app.run(debug=True)
