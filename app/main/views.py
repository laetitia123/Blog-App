
# from flask import render_template,request,redirect,url_for
from . import main
import requests
from ..requests import getQuotes

from ..forms import ReviewForm
from ..models import Quotes
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import Blog, User
from .forms import BlogForm,UpdateProfile
from .. import db,photos
from flask_login import login_required, current_user

import markdown2 
@main.route('/review/<int:id>')
def single_review(id):
    review=Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# Views
@main.route('/')
def index():

    # blogs =Blog.get_blogs()
    try:
       quotes = getQuotes()
    except Exception as e:
       quotes = "quotes unavailable"
       title='Welcome to blog'
    return render_template('index.html',quotes = quotes)


@main.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html',title = title,movie = movie,reviews = reviews)



@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)






@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    # my_upvotes = Upvote.query.filter_by(blog_id = Blog.id)
    if form.validate_on_submit():
        blog = form.blog.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)

        new_blog=Blog(user_id =current_user._get_current_object().id, blog=blog,category=category)
        db.session.add(new_blog)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('blog.html',form=form)


@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comment.html', form = form, comment = all_comments, pitch = pitch )

