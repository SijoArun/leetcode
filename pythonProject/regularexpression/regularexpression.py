import re

str="Take 1 One idea 1-2-2012.One 2 idea at a time 12-10-2022"
result=re.search(r'o\w\w',str)
print(result)

result=re.findall(r'o\w\w',str)
print(result)

result=re.match(r'T\w\w\w',str)
print(result.group)

result=re.split(r'\d+',str)
print(result)

result=re.sub(r'One','Two',str)
print(result)

result=re.findall(r'O\w{2}',str)
print(result)
result=re.findall(r'O\w{1,2}',str)
print(result)

result=re.findall(r'O\w+',str)
print(result)

result=re.findall(r'O\w*',str)
print(result)

result=re.findall(r'O\w?',str)
print(result)

result=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

result=re.search(r'^T\w*',str)
print(result.group())