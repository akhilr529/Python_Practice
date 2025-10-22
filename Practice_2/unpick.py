import pickle
f = open("emp.dat", "rb")
print("Employee Details:")
while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print("All employees completed")
        break
f.close()