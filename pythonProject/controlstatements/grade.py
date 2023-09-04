maths=int(input("Enter the maths score\n"))
physics=int(input("Enter the physics score\n"))
chemistry=int(input("Enter the chemistry score\n"))
totalavg=(maths+physics+chemistry)/3;

if (maths<=35 or physics<=35 or chemistry<=35):
    print("You failed in exam")
else:
    print("You passed in exam")
    if(totalavg<=59):
        print("Grade is c")
    elif(totalavg<=69):
        print("Grade is B")
    else:
        print("Grade is A")
