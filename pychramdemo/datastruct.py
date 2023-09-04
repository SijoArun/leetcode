students = {'john': ['python', 'DRF'], 'bob': ['java', 'springboot'], 'peter': ['js', 'node']}
key=students.keys()
for eachkey in key:
    print('courses taken by ',eachkey,' are : ' )
    for eachcourse in students[eachkey]:
        print(eachcourse)

