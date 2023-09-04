class ATMconstant:
    withdraw=1
    balancecheck=2
    deposit=3
option=int(input("Enter the option "))
match option:
    case ATMconstant.withdraw:
        print("withdraw")
    case ATMconstant.balancecheck:
        print("balancecheck")
    case ATMconstant.deposit:
        print("deposit")
    case _:
        print("Invalid option")

