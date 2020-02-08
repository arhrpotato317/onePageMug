from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# MongoDB 연결
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')



# 주문하기 API (POST API) - request body 요청
@app.route('/order', methods=['POST'])
def order_post():
    name_receive = request.form['name']
    count_receive = request.form['count']
    address_receive = request.form['address']
    phone_receive = request.form['phone']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.order.insert_one(doc)

    return jsonify({'result': 'success'})

# 주문보기 API (GET API)
@app.route('/order', methods=['GET'])
def order_get():
    all_order = list(db.order.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'all_order': all_order})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)