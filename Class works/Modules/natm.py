import iATM as a
#(or) import iATM (or) from iATM import login, checkbalance,deposit,withdraw,viewTransactions (or) import iATM * (imports all functions)
u_pin= int(input("Enter the pin: "))

if a.login(u_pin):

    while True:
        print('\n\n\n')
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("0. Exit")

        ch = int(input("Enter the choice: "))
        if ch==1:
            a.checkbalance(u_pin)
        elif ch==2:
            a.deposit(u_pin)
        elif ch==3:
            a.withdraw(u_pin)
        elif ch==4:
            a.viewTransactions(u_pin)
        elif ch==0:
            print("Thankyou")
            break
        else:
            print("Invalid choice")