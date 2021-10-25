import time

def timeLength(name, function):
    startTime = time.time()
    function()
    endTime = (time.time() - startTime)
    return endTime


