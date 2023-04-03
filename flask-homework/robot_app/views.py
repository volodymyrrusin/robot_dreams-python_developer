import werkzeug.exceptions
import random
from robot_app import app
from flask import request, redirect


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
        users_result = [random.choice(users_list) for _ in range(random.randrange(100))]
    return f'List of users: {users_result}', 200


@app.route('/books')
def get_books():
    books_list = ['Kobzar', 'Harry Potter', 'The Witcher']
    books_html = """
    <div>List of books:</div>
    <ul>
    """
    if request.args.get('count'):
        books_count = int(request.args.get('count'))
        for _ in range(books_count):
            books_html += f'<li>{random.choice(books_list)}'
    else:
        for _ in range(random.randrange(100)):
            books_html += f'<li>{random.choice(books_list)}'
    books_html += '</ul>'
    return books_html, 200


@app.route('/users/<int:user_id>')
def get_user(user_id):
    if user_id % 2 == 0:
        return f'{user_id}', 200
    else:
        return '', 404


@app.route('/books/<string:book_title>')
def get_book(book_title):
    return f'{book_title.title()}', 200


@app.route('/params')
def params_query():
    params_table = ('<table>'
                    '<thead>'
                    '<tr>'
                    '<th>parameter</th>'
                    '<th>value</th>'
                    '</tr>'
                    '</thead>')
    for key, value in request.args.items():
        params_table += ('<tr>'
                         f'<th>{key}</th>'
                         f'<th>{value}</th>'
                         '</tr>')
    params_table += '</table>'
    return params_table, 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        html_form = """
        <form method=POST action='/login'>
            <input type='string' name='username' value='' minlength='5'/>
            <input type='password' name='password' value='' minlength='8' pattern='^(.*[A-Z])(.*[0-9]).*$'/>
            <button type='submit'>Submit</button>
        </form>        
        """
        return html_form, 200
    elif request.method == 'POST':
        if request.form['username'] and request.form['password']:
            return redirect('/users')
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
    html_code = """
    <div><a href="http://127.0.0.1:5000/login">Login</a></div>
    <div><a href="http://127.0.0.1:5000/users">Users</a></div>
    <div><a href="http://127.0.0.1:5000/books">Books</a></div>
    <div><a href="http://127.0.0.1:5000/params">Params</a></div>
    """
    return html_code, 200


