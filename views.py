from app import app
from flask import Flask, render_template, request, abort
from flask_babel import Babel, gettext
# from config import Config


babel=Babel(app)

@babel.localeselector
def get_local():
    # return 'pl'
    return request.accept_languages.best_match(['ua', 'en', 'pl'])



# @babel.localeselector
# def get_locale():
#     return request.accept_languages.best_match(Config.LANGUAGES.keys)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user/<name>')
@app.route('/user/')
def user(name=None):
    if name is None:
        name=request.args.get('name')
    if name:
        return render_template('hello.html', name=name)
    else:
        abort(404)