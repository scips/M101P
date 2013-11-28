from bottle import route, run, template

@route('/hello/<name>')
def index(name='World'):
    return template('<strong>Hello {{name}}</strong>!', name=name)

run(host='localhost', port=8080, debug=True)
