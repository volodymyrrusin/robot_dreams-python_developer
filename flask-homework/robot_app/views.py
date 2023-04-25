import werkzeug.exceptions
from robot_app import app, db
from flask import request, redirect, render_template, session, url_for
from .models import *

app.secret_key = b'some_secret_key'


@app.route('/hello')
def hello():
    app.logger.info('Hello world is called')
    return 'Hello, world!'


@app.route('/users')
def get_users():
    size = request.args.get('size')
    if size:
        query = db.Select(User).limit(size)
        users = db.session.scalars(query)
    else:
        users = User.query.all()
    username = session.get('user')
    if username:
        return render_template('users.html', users=users, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/books')
def get_books():
    size = request.args.get('size')
    if size:
        query = db.Select(Book).limit(size)
        books = db.session.scalars(query)
    else:
        books = Book.query.all()
    username = session.get('user')
    if username:
        return render_template('books.html', books=books, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    username = session.get('user')
    if username:
        return render_template('user_id.html', user=user, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/books/<string:book_id>')
def get_book(book_id):
    book = db.get_or_404(Book, book_id)
    username = session.get('user')
    if username:
        return render_template('book_id.html', book=book, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/purchases')
def get_purchases():
    size = request.args.get('size')
    if size:
        query = db.Select(Purchase).limit(size)
        purchases = db.session.scalars(query)
    else:
        purchases = Purchase.query.all()
    username = session.get('user')
    if username:
        return render_template('purchases.html', purchases=purchases, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/purchases/<int:purchase_id>')
def get_purchase(purchase_id):
    purchase = db.get_or_404(Purchase, purchase_id)
    username = session.get('user')
    if username:
        return render_template('purchase_id.html', purchase=purchase, username=username)
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


@app.route('/users', methods=['POST', ])
def create_users():
    user = User(
        first_name=request.form.get('first_name'),
        last_name=request.form.get('last_name'),
        age=request.form.get('age')
    )
    db.session.add(user)
    db.session.commit()
    return 'User created', 201


@app.route('/books', methods=['POST', ])
def create_books():
    book = Book(
        title=request.form.get('title'),
        author=request.form.get('author'),
        year=request.form.get('year'),
        price=request.form.get('price')
    )
    db.session.add(book)
    db.session.commit()
    return 'Book created', 201


@app.route('/purchases', methods=['POST', ])
def create_purchases():
    user_id = request.form.get('user_id')
    user = db.get_or_404(User, user_id)
    book_id = request.form.get('book_id')
    book = db.get_or_404(Book, book_id)
    purchase = Purchase(
        user_id=user.id,
        book_id=book.id,
        date=request.form.get('date')
    )
    db.session.add(purchase)
    db.session.commit()
    return 'Purchase created', 201
