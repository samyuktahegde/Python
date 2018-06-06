from bottle import run, route

@route('/')
def index():
    # return '<h1>HTML</h1>'
    # return {'name':'jsonData', 'myList':[1,2,3,4,5]}
    return 'Hello'

run(debug=True, reloader=True)