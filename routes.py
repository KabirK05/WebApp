from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
{
        'author': 'SoccerCapitan8',
        'title': 'When THey Dropping The Jordan 4s?',
        'content': 'Bro I swear they should drop the red thunders like literally tomorrow But .',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Fireydiamond',
        'title': 'Boi What da Hell Boi',
        'content': 'Im Just wanna get the Black Cat 4s but they cost like $600. Anyone know nay place i can get them for cheaper?',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'TheSneakerKnockerz101',
        'title': 'When THey Dropping The Jordan 4s? reply:',
        'content': 'They should be droping them on October 4th so just gotta wait but you also are gonna have to hope that you can even manage to get your hands on a pair.',
        'date_posted': 'April 20, 2018'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)