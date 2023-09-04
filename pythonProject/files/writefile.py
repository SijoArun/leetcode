f=open("myfile.txt","w")
print("Enter the text untill the #")
s=''
while s!="#":
    s=input()
    f.write(s+"\n")
f.close()