import pymongo
from pymongo import MongoClient
from datetime import datetime
#mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
#url = 'mongodb://[admin:123456@]192.168.0.102[:27017][/[admin]'
#uri = 'mongodb://admin:123456@192.168.0.102:27017/admin'
try:
	client = MongoClient('mongodb://blogadmin:123456@192.168.0.102:27017/blog')
	#下面的这两个是有相同的效果的
	#blog=client['blog']
	blog=client.blog
	print("数据库连接成功")
except Exception:
	print("数据库连接失败")
result = blog.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)
print(result.inserted_id)