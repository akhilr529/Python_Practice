
def f1():
    print("f1 execution")
def f2():
    print("f2 execution")

def f3():
    print("f3 execution")

f2()
f1()
f3()

if __name__ == "__main__":
    print("Direct Execution like main")
else:
    print("Indirect exection because import")