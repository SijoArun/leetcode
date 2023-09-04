dict1 = {1: "john", 2: "mayank", 3: "dhaval"}
print(dict1)

print(dict1[2])

key = dict1.keys()
for i in key:
    print(i)

value = dict1.values()
for i in value:
    print(i)

del dict1[2]

print(dict1)
