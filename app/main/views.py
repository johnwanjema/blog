from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
from ..models import Blog, User
from flask_login import login_user, logout_user, login_required, current_user
from .forms import BlogForm


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/new_blog', methods=['GET', 'POST'])
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog=form.blog.data, blog_title=form.blog_title.data,
                    blog_upvotes=0, blog_downvotes=0)
        blog.save_blog
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
        title="pitches"
    return render_template('new_blog.html', blog_form=form)
