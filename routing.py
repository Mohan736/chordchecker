from flask import Flask
from flask.templating import render_template
from flask.blueprints import Blueprint

routing = Blueprint('routing', __name__, template_folder='templates')

@routing.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@routing.route('/')
def home():
    return render_template('acceuil.html')

@routing.route('/about')
def about():
    return render_template('about.html')

@routing.route('/resources')
def resources():
    return render_template('resources.html')

@routing.route('/songs')
def songs():
    return render_template('songs.html')

@routing.route('/learn')
def learn():
    return render_template('learn.html')

@routing.route('/login')
def login():
    return render_template('login.html')

@routing.route('/sitemap.xml')
def sitemap():
    return render_template('2325984_5.xml')
