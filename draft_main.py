import csv
import json
from flask import Flask, jsonify
from items import Items 

app = Flask(__name__)

#add parse function to convert csv file to json obj
listings = [
    {
        'id': 1,
        'title': u'item1',
        'description': u'??????', 
        'price': 8.0
    },
    {
        'id': 2,
        'title': u'item2',
        'description': u'???????', 
        'price': 7.0
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': listings})

if __name__ == '__main__':
    app.run(debug=True)