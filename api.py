from flask import Flask,jsonify
from db.mongoeng import Log
from db.settings import mg_lottery

app = Flask(__name__)

def lastest(uid):
    last_time = mg_lottery.find({'uid':uid},{'_id': 0}).sort('add_time', direction=-1)
    return list(last_time)[0]

@app.route('/')
def index():
    # ids
    lottery_ids = ['001', '113', '002', '106']
    datas = [lastest(x) for x in lottery_ids]

    return jsonify(datas)


@app.route('/<uid>')
def dtails(uid):
    uid = str(uid)
    data = lastest(uid)
    return jsonify(data)

if __name__ == '__main__':
    app.run()