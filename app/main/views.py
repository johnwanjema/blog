from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from .. import db
from ..models import Blog, User, Comment
from flask_login import login_user, logout_user, login_required, current_user
from .forms import BlogForm, CommentForm


@main.route('/')
def index():

    blogs = Blog.query.all()
    print(blogs)
    if blogs is None:
        return redirect(url_for('main.new_blog'))
        flash("no blogs")
    return render_template("index.html", blogs=blogs)


@main.route('/new_blog', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog=form.blog.data, blog_title=form.blog_title.data,
                    blog_upvotes=0, blog_downvotes=0)
        blog.save_blog
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', blog_form=form)


@main.route('/new_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = Blog.get_blog(id)
    comments = Comment.get_comments(id)
    print(comments)
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, blog_id=blog.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
        title="pitches"
    return render_template('new_comment.html', comment_form = form,comments = comments)
