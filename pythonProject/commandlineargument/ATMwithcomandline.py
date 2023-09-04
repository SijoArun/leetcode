import sys
lst=sys.argv

accbal=10000

for i in lst:
    print("Available option in ATM")
    if(lst[i] == 1):
          print("1.Check Balance")
    if(lst[i]== 2):
        print("1.WithDraw")
    if (lst[i] == 3):
        print("1.Deposit cash")
    if (lst[i] == 4):
        print("1.Deposit cheque")

case=int(input("Please select the valid option"));


def calculate(case,accbal):
    switcher = {
        "1":"Available Balance in ATM"+accbal,
        "2": "Enter the withdraw amount",
        "3": "Enter the deposit amount",
        "4": "Enter the deposit cheque amount"

    }
    message= switcher.get(case, "Invalid input")
    if case == '2':
        wamount=int(input())
        accbal=accbal-wamount
        print("Amount withdrawn successfully, updated balance is "+accbal)

    if case == '3':
        ddamount = int(input())
        accbal = accbal + ddamount
        print("Amount deposited successfully, updated balance is " + accbal)

    if case == '4':
            dcamount = int(input())
            accbal = accbal + dcamount
            print("Amount deposited successfully, updated balance is " + accbal)

calculate(case,accbal)




