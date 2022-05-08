from flask import render_template
from app.main import auth

@auth.route('/')
def index():
    return render_template('index.html')