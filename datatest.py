import time

document={
        "type" : "Java",
        "title" : "HelloWorld",
        "content" : "关于java的学习",
        "url":"/145236479811sedrggfs",
        "datetime" : time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
}
#update_doc={'id':123456789,'name':'lisi','age':23}
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
# newtime=GetNowTime()
if __name__ == '__main__':
    from DBmanage import dbmanage
    #import time
    user='blogadmin'
    pwd='123456'
    host='192.168.0.107'
    port='27017'
    database='blog'
    #mongodb://blogadmin:123456@192.168.0.102:27017/blog
    d=dbmanage(user,pwd,host,port,database)
    conn=d.connection()
    #result=d.query({'type':'Java'})
    #results=d.query_all()
    d.insert_one(document)
    # for result in results:
    #     print(result['_id'],end="")
    #     print(result['title'])
    #d.delete(document)
    #cols=d.queryall()
    # if cols is not None:
    #     for col in cols:
    #         print(col['title'])
    # d.update_one(update_doc)