# import dbtools
from dbtools import Db

db = Db("192.144.148.91","ljtest","123456","ljtestdb")
a = db.chaxun("show tables;")
print(a)