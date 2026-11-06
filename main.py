#ATM STIMULATION

balance=10000
#LIST
transactions=[]

#FUNCTION TO CHECK BALANCE
def check_balance():
    print(f"current balance:Rs.{balance}")

#FUNCTION TO DEPOSIT
def deposit():
    global balance
    amount=float(input("enter amount to deposit:Rs."))
    balance+=amount
    transactions.append(f"deposited{amount}")
    print("deposited successfully.")

#FUNCTION TO WITHDRAW
def withdraw():
    global balance
    amount=float(input("enter amount to withdraw:Rs."))
    if amount>balance:
        print("insufficient balance!")
    else:
        balance-=amount
        transactions.append(f"withdrawn{amount}") 
        print("withdrawal successful.")   

#FUNCTION TO TRANSACTION HISTORY
def transaction_history():
    if len(transactions)==0:
        print("no transaction found.")
    else:
        print("transaction history:")
        for transaction in transactions:
            print(transaction)


while True:
    print("\n------ATM menu-----")
    print("1.check balance")
    print("2.deposit amount")
    print("3.withdraw amount")
    print("4.transaction history")
    print("5.exit")
    choice=input("enter your choice:")
    if choice=="1":
        check_balance()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        transaction_history()
    elif choice=="5":
        print("exit.") 
        break     
    else:
        print("invalid choice.") 