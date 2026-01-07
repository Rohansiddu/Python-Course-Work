data= {
    1234: {'balance':2000,'transactions':[]},
    2341: {'balance':90000,'transactions':[]},
    3421: {'balance':56000,'transactions':[]},
   }

def login(pin):
    if pin in data:
        print("Login Successful")
        return True
    else:
        print("Invalid pin. Try Again!!!")
        return False

def checkbalance(pin):
    print(f"Balance Amount: ${data[pin]['balance']}")

def deposit(pin):
    amount = int(input("Enter the amount: "))
    data[pin]['balance']+=amount
    data[pin]['transactions'].append(f'${amount} is deposited++++++')
    print("Deposit Successful")

def withdraw(pin):
    amount = int(input("Enter the amount: "))
    if amount <= data[pin]['balance']:
        data[pin]['balance']-=amount
        data[pin]['transactions'].append(f'${amount} is withdraw-----')
        print("Amount is Withdraw successful")
    else:
        print("Insufficinet Balance")

def viewTransactions(pin):
    if data[pin]['transactions']:
        print("Transaction Histroy: ")
        for i in data[pin]['transactions']:
            print(i)
        else:
            print("End of Transactions")
    else:
        print("No Transactions")