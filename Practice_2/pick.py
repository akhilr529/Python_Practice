import pickle, emp
f=open("emp.dat", "wb")
n=int(input("Enter number of employees: "))
for i in range(n):
    eno = int(input("Enter employee number: "))
    ename = input("Enter employee name: ")
    esal = float(input("Enter employee salary: "))
    eaddr = input("Enter employee address: ")
    e = emp.Employee(eno, ename, esal, eaddr)
    pickle.dump(e, f)
print("Employee objects pickled successfully")
f.close()