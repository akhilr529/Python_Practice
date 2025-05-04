from emp import Employee
import pickle

with open("emp.ser", "wb") as f:
    while True:
        eno = int(input("Enter ENO: "))
        ename = input("Enter ENAME: ")
        esal = float(input("Enter ESAL: "))
        eaddr = input("Enter EADDR: ")
        e = Employee(eno, ename, esal, eaddr)
        pickle.dump(e, f)
        option = input("Do you want ot serialize another employee object[Yes/No]?")
        if option.lower() == "no":
            break
    print("Multiple employee object serialized")