from bottle import Bottle
from bottle.ext.mongo import MongoPlugin

app = Bottle()
db_plugin = MongoPlugin(uri='mongodb://127.0.0.1:27017/', db='local')
app.install(db_plugin)

@app.route('/')
def index(mongodb):
    mongodb['test_collection'].insert({'key':'value1'})
    mongodb['test_collection'].insert({'key':'value2'})
    return 'Inserted data'

@app.route('/get')
def get_all(mongodb):
    query = mongodb['test_collection'].find()
    results = []
    for q in query:
        results.append(q['key']) 
    return {'result':results}       

app.run(debug=True, reLoader=True)
