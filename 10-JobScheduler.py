import time

def scheduler(function, n):
    print("Begin time is: " + time.ctime())
    time.sleep(n/1000)
    print("End time is: " + time.ctime())
    function()

def function():
    print("Hello, world!")

scheduler(function, 1000)