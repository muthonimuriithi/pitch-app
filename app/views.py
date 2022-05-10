from flask import render_template
from app.main import auth
from .models import Pitch


@auth.route('/')
def index():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category = 'Job').all() 
    event = Pitch.query.filter_by(category = 'Events').all()
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    return render_template('index.html', job = job, event = event, pitches = pitches,advertisement= advertisement)

    

   