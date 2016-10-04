import time

#返回当前时间

def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
newtime=GetNowTime()
print(newtime)