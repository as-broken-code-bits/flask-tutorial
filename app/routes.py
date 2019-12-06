from app import app
from flask import render_template

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
