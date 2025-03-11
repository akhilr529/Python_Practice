from sys import argv
# print(type(argv))
# print(argv)
# print(argv[1])

#Program to print command line arguments information
# print("The number of cmd line arguments", len(argv))
# print("List of cmd line arguments", argv)
# print("The cmd line arguments one by one")
# for x in argv:
#     print(x)


#Program to print sum of given numbers provided as cmd line arguments
sum =0
for x in argv[1:]:
    sum = sum+ int(x)
print("The sum=",sum)