from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'A'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'John says things'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'Susan says things'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
