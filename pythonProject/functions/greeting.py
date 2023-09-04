def display(name):
    def message():
        return "Hello "
    result= message()+name
    return result

c=display("sijo")
print(c)