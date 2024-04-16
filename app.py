from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello_world():
    return "Hello World"

@app.route('/user/<username>')
def show_user_profile(username: str):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    return f'Post {escape(post_id)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'