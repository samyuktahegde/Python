from bottle import route, run, request

@route('/querytest')
def querytest():
    param1 = request.query.param1
    param2 = request.query.param2
    return '<h1>The value of param1 is:'+param1+' and value of param2 is:'+param2+'</h1>'

if __name__ == '__main__':
    run(debug=True, reloader=True)

