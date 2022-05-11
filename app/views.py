from flask import render_template
from app.main import auth
# from app.models.models import Post, Comment, User, Upvote, Downvote



@auth.route('/')
def index():
    
    # posts = Post.query.all()
    # product = Post.query.filter_by(category='product').all()
    # idea = Post.query.filter_by(category='idea').all()
    # business = Post.query.filter_by(category='Business').all()
    # return render_template('index.html', business=business, product=product, idea=idea, posts=posts)

    return render_template('index.html' )

   