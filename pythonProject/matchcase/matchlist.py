list=["python","Django","dockor","drf"]

match list:
    case ["python","Django"]:
        print("one")
    case ["dockor","Django"]:
        print("Two")
    case ["python","Django","dockor","drf"]:
        print("Three")
    case _:
        print("Default")

