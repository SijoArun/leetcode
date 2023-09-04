def customgen(x,y):
    while x<y:
        yield x
        x=x+1

result= customgen(10,20)

for i in result: print(i)