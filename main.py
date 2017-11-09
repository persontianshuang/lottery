from datetime import datetime

from db.settings import mg_lottery
from extra import Shuangseqiu, Fucai3d, Daletou, Jiangxi11xuan5
from req import get_html

from db.mongoeng import Log

response = get_html()

datas = [Shuangseqiu(response).main(),
Daletou(response).main(),
Fucai3d(response).main(),
Jiangxi11xuan5(response).main()]


def sk(x):
    ticket = Log()
    ticket.uid = x['id']
    ticket.des = x['des']
    ticket.progress = x['progress']
    ticket.check_time = x['check_time']
    ticket.lottery_num = x['lottery_num']
    ticket.save()

[sk(k) for k in datas]

# print(Log.objects(uid='001').order_by('-add_time').first().add_time)