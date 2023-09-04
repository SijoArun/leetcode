lst = [10, 20, "test", -12, 12.12]
print(lst)
print(lst[2])
print(len(lst))
print(lst[2:5])

lst.append(40)
print(lst)

lst.remove("test")
print(lst)

del (lst[0])
print(lst)

# lst.clear()
# print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 99)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)
