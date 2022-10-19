# test
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:sparta@cluster0.7din7v3.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/pecel", methods=["POST"])
def pecel_post():
    pecel_receive = request.form['pecel_give']

    count = db.pecel.count_documents({})
    num = count + 1

    doc = {
        'num': num,
        'pecel': pecel_receive,
        'done': 0,
    }
    db.pecel.insert_one(doc)
    return jsonify()

@app.route("/pecel/done", methods=["POST"])
def pecel_done():
    num_receive = request.form['num_give']
    db.pecel.update_one(
        {'num': int(num_receive)},
        {'$set': {'done': 1}}
    )
    return jsonify()

@app.route("/pecel//cancel", methods=["POST"])
def cancel_pecel():
    num_receive = request.form['num_give']
    db.pecel.update_one(
        {'num': int(num_receive)},
        {'$set': {'done': 0}}
    )
    return jsonify()

@app.route("/delete", methods=["POST"])
def delete_pecel():
    num_receive = request.form['num_give']
    db.pecel.delete_one({'num': int(num_receive)})
    return jsonify()

@app.route("/pecel", methods=["GET"])
def pecel_get():
    pecels_list = list(db.pecel.find({}, {'_id': False}))
    return jsonify({'pecels': pecels_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)