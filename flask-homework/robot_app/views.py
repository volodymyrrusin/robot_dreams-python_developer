from robot_app import app


@app.route('/hello')
def hello():
    app.logger.info('Hello world is called')
    return 'Hello, world!'
