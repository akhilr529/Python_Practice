import inspect
def getInfo():
    print(inspect.stack())
    print("------------------------------")
    print(inspect.stack()[1])
    print("------------------------------")
    print("Caller Module :", inspect.stack()[1][1])
    print("------------------------------")
    print("caller function Name :", inspect.stack()[1][3])