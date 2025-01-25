# nhận tiền
def deposit(): 
    amount= float(input("Enter an amount to be deposited: "))
    if amount<0:
        print("*******************")
        print("Error")
        return 0
    else:
        print("*******************")
        print(f"Receive success ${amount:.2f}")
        return amount

# xem số dư
def show_balance(balance):
    print(f"Available balance: ${balance}")
    return show_balance

# rút tiền
def withdraw(balance):
    amount= float(input("Enter an amount to be withdraw: "))
    if amount<0:
        print("*******************")
        print("Error")
        return 0
    elif amount>balance:
        print("*******************")
        print("Balance not enough")
        return 0
    else:
        print("*******************")
        print(f"Withdraw success {amount:.2f}" )
        print("your available balance is ",balance-amount)
        return amount

# màn chính
def main():
    balance=0
    is_running =True
    while is_running:
        print("*******************")
        print("Banking Program")
        print("*******************")
        print("1.Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*******************")
        choice= input("Enter your choice(1-4): ")
        print("*******************")
        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance+=deposit()
        elif choice=='3':
            balance-=withdraw(balance)
        elif choice=='4':
            print("Thank!")
            print("*******************")
            is_running= False
        else:
            print("Error! Please choice between 1 and 4")
main()