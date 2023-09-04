f=open("sample.txt","r+")
print(len(f.readlines()))
f.seek(0)
print(len(f.read().split("\n")))