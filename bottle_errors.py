from bottle import route, run, error

@error(404)
def error404(error):
    return '<h1>You have experienced a 404</h1>'

@error(405)
def error405(error):
    return '<h1>This method is not allowed</h1>'

@error(500)
def error500(error):
    return '<h1>Something went wrong</h1>'


@route('/', method='POST')
def index():
    return '<h1>index</h1>'

@route('/zero')
def zero():
    return 1/0

run(debug=False, reloader=True)
