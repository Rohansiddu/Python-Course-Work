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
    


u_pin= int(input("Enter the pin: "))

if login(u_pin):

    while True:
        print('\n\n\n')
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("0. Exit")

        ch = int(input("Enter the choice: "))
        if ch==1:
            checkbalance(u_pin)
        elif ch==2:
            deposit(u_pin)
        elif ch==3:
            withdraw(u_pin)
        elif ch==4:
            viewTransactions(u_pin)
        elif ch==0:
            print("Thankyou")
            break
        else:
            print("Invalid choice")
        

