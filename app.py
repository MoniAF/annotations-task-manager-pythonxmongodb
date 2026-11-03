from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['AnnotationsDB']
collection = db['tasks']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            datetask = request.form['datetask']
            name = request.form['name']
            description = request.form['description']
            priority = request.form['priority']
            
            data = {'datetask': datetask, 'name': name, 'description': description, 'priority': priority}
            collection.insert_one(data)
            return redirect('/tasks')
        except ValueError as e:
            return f'Error: {e}. Please check your input.'
        except Exception as e:
            return f'Error: {e}. An unexpected error occurred.'
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    datos = list(collection.find())
    return render_template('tasks.html', datos=datos)

@app.route('/updatetask/<id>', methods=['GET'])
def show_update_form(id):
    dato = collection.find_one({'_id': ObjectId(id)})
    return render_template('updatetask.html', dato=dato)

@app.route('/updatetask/<id>', methods=['POST'])
def update(id):
    datetask = request.form['datetask']
    name = request.form['name']
    description = request.form['description']
    priority = request.form['priority']
    
    collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'datetask': datetask, 'name': name, 'description': description, 'priority': priority}}  
    )
    
    return redirect('/tasks')

@app.route('/delete/<id>', methods=['POST'])
def delete_tasks(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect('/tasks')

if __name__ == '__main__':
    app.run(debug=True)