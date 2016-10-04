import pymongo
from pymongo import MongoClient


class dbmanage:
	"""数据库管理类实现对数据库进行增删改查"""


	def  __init__(self,name,pwd,ip,port,database):
		self.url=port
		self.pwd=pwd
		self.name=name
		self.ip=ip
		self.port=port
		self.database=database
	def connection(self):
		self.dataurl='mongodb:'+'//'+self.name+':'+self.pwd+'@'+self.ip+':'+self.port+'/'+self.database
		#print(self.dataurl)
		try:
			#conn= MongoClient('mongodb://blogadmin:123456@192.168.0.102:27017/blog')
			self.conn=MongoClient(self.dataurl)
			self.database=self.conn[self.database]
			#print(self.database)
		except Exception:
			print("连接失败")

	def insert_one(self, blogs):
		#use=users()
		self.database.blog.insert_one(blogs)
		return 0

	def insert_many(self, manyuser):
		self.database.user.insert(manyuser)
		return 0

	def query(self, keyvalue):
		result = self.database.blog.find_one(keyvalue)
		return result

	def query_all(self):
		results=self.database.blog.find().limit(10)
		return results

	def delete(self, keyvalue):
		self.database.user.remove()
		return

	def update_one(self,keyvalue):
		db.Employees.update_one(
        {"id": keyvalue},
        {
        "$set": {
            "name":name,
            "age":age,
            "country":country
        }
        }
    )
		print(keyvalue)
		self.database.doc_user.update(keyvalue)

