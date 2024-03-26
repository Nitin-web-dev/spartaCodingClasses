from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://nitinwebdev5:Xfv69huNHzvRhVyB@cluster0.iqvlhdl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbhomework

@app.route('/')
def home():
   return render_template('index.html')

# to insert data in database
@app.route("/mars", methods=["POST"])
def web_mars_post():
    user_name = request.form['name_give']
    user_address = request.form['address_give']
    plot_size = request.form['size_give']
                 
    doc = {
        'name':user_name,
        'address': user_address,
        'size': plot_size
    }
    db.mars.insert_one(doc)
    return jsonify({'msg': 'order addead'})

#  to get data from database
@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders = list(db.mars.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})
    

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)