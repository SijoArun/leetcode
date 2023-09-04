studentid=int(input("Enter the id"))
studentname=(input("Enter the name"))
a,b,c=[float(x) for x in input("Enter the 3 marks").split(",")]
average=float((a+b+c)/3)
print(average)