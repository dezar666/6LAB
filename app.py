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
    return 'Search page'


@app.route('/about/')
def about():
    return 'About page'


if __name__ == '__main__':
    app.run(debug=True)
