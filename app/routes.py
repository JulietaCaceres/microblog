from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'juli'}
    posts = [
        {'user': 'javi',
         'post': 'trump gana las elecciones de nuevo'},
        {'user': 'luci',
        'post': 'me dieron alta torta'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for the user {}, remember_me {}'.format(form.username.data, form.remember_me.data))
        return  redirect(url_for('login'))
    return render_template("login.html", title='Sign In', form=form)
