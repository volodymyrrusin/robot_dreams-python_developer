import werkzeug.exceptions
import random
from robot_app import app
from flask import request, redirect, render_template, session, url_for

app.secret_key = b'some_secret_key'

@app.route('/hello')
def hello():
    app.logger.info('Hello world is called')
    return 'Hello, world!'


@app.route('/users')
def get_users():
    users_list = ['Taras', 'Joanne', 'Andrzej']
    if request.args.get('count'):
        users_count = int(request.args.get('count'))
        users_result = [random.choice(users_list) for _ in range(users_count)]
    else:
        users_count = random.randrange(100)
        users_result = [random.choice(users_list) for _ in range(users_count)]
    username = session.get('user')
    if username:
        return render_template('users.html', users=users_result, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/books')
def get_books():
    books_list = ['Kobzar', 'Harry Potter', 'The Witcher']
    if request.args.get('count'):
        books_count = int(request.args.get('count'))
        random_book = [random.choice(books_list) for _ in range(books_count)]
    else:
        books_count = random.randrange(100)
        random_book = [random.choice(books_list) for _ in range(books_count)]
    username = session.get('user')
    context = {
        'books_count': books_count,
        'random_book': random_book,
        'username': username
    }
    if username:
        return render_template('books.html', **context)
    else:
        return redirect(url_for('login'))


@app.route('/users/<int:user_id>')
def get_user(user_id):
    if user_id % 2 == 0:
        username = session.get('user')
        if username:
            return render_template('user_id.html', user_id=user_id, username=username)
        else:
            return redirect(url_for('login'))
    else:
        return '', 404


@app.route('/books/<string:book_title>')
def get_book(book_title):
    book_title = book_title.title()
    username = session.get('user')
    if username:
        return render_template('book_title.html', book_title=book_title, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/params')
def params_query():
    username = session.get('user')
    if username:
        return render_template('params.html', attributes=request.args, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if request.form['username'] and request.form['password']:
            username = request.form.get('username')
            session['user'] = username
            return redirect(url_for('get_users'))
        else:
            return 'No information', 400
    else:
        return 'Bad Request', 400


@app.errorhandler(werkzeug.exceptions.NotFound)
def default_404(e):
    return 'Page not found'


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def default_500(e):
    return 'Server can not fulfill the request'


@app.get('/')
def get_handler():
    return render_template('main_page.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))