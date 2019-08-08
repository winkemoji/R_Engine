from os import abort

from flask import Flask, jsonify


class FeatureModule:
    def __init__(self):
        pass


class RecommendModule:
    def __init__(self):
        pass


class FilteringModule:
    def __init__(self):
        print('init FilteringModule')
        pass


class HttpContextModule:
   def __init__(self):
        print('init HttpContextModule')
        app = Flask(__name__)

        tasks = [
            {
                'id': 1,
                'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                'done': False
            },
            {
                'id': 2,
                'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on the web',
                'done': False
            }
        ]

        @app.route('/aya/api/v1.0/tasks', methods=['GET'])
        def index():
            return jsonify({'tasks': tasks})

        @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
        def get_task(task_id):
            task = filter(lambda t: t['id'] == task_id, tasks)
            if len(task) == 0:
                abort(404)
            return jsonify({'task': task[0]})

        app.run(debug=True)
        pass