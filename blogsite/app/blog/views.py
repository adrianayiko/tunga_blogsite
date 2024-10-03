from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import blog
from .forms import PostForm
from app.models import Post
from app import db

@blog.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@blog.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data, author_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template('new_post.html', form=form)
