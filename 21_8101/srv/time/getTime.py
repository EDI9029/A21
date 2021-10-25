import time

def getTime():
    localtime = time.localtime()
    result = time.strftime("%H:%M:%S", localtime)
    return(result)

def getDate():
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d", localtime)
    return(result)