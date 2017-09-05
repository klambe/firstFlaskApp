from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'my wonderful store',
        'items': [
            {
                'name': 'my Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return 'home Page not wired up!'


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({'message':'store not found'})


@app.route('/store')
def get_all_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = request_data['items']
            store['items'].append(new_item)
            return jsonify(store)

    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])

    return jsonify({'message':'store not found'})


app.run(port=5000)
