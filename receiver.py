import pickle
print("Deserialization emp object & printing data\n")
with open("emp.ser", "rb") as f:
    while True:
        # e = pickle.load(f)
        # e.display()
        try:
            e = pickle.load(f)
            e.display()
        except EOFError:
            break
    print("All Employees completed")