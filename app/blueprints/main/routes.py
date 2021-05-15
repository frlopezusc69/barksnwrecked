from . import bp as main
from flask import render_template

@main.route('/')
def index():
    return "Hello World!"