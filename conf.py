# -*- encoding:utf-8 -*-
import json
# 如果在python3.4下报错就要加上codecs.open('','','utf-8')
import codecs


class Config(object):
	"""本类是用来读取配置信息并且转化为json数据的"""
	def __init__(self):
		pass

	#读取配置文件并且转化为字符串
	def read_file(self,path):
		conf_file=codecs.open(path, "r",'utf-8')
		#f=codecs.open("./conf/pymongo.conf","r",'utf-8')
		self.string="".join(conf_file.readlines())
		f.close()
		return self.string

	#将字符串转换为json
	def convert_json(self):
		self.json=json.loads(self.string)
		return self.json
class DatabaseInfo(object):
	"""通过获取的conf文件信息来获取数据库的连接信息"""
	def __init__(self):
		pass
connObject=json.loads(stringjson)
	def if_Mongo(self):
		
		
print(len(connObject["hosts"]))

#print(connObject["hosts"][1]['host'])
#data_string = json.dumps(f)
# print(data_string)
# for line in f.readlines():
# 	print(line)
#data_string=json.dump(lst)
#print(lst)
#print(data_string)
# if conf["id"] not is 'mongodb':
	print("读取配置文件错误")
	return -1



