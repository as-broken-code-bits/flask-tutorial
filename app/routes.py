from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'A'}
    return """
    <html>
        <head>
            <title> Home page - Microblog </title>
        </head>
        <body>
            <h1> Hello """ + user['username'] + """!</h1>
        </body>
    </html>
    """