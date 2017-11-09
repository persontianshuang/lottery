from datetime import datetime

from mongoengine import *
from db.settings import MG_COLL,MG_HOST,MG_PORT

connect(MG_COLL,host=MG_HOST,port=MG_PORT)

class Log(Document):
    uid = StringField()
    des = StringField()
    progress = StringField()
    check_time = StringField()

    add_time = DateTimeField(default=datetime.now)