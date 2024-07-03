# import time 

# print("Please insert your Card")
# time.sleep(5)
# password = 1234
# pin = int(input("Enter your atm pin"))


# print("Enter your amount :-5000 ")

# if pin == password:
#     while True:
            
#         print("""
#             1 == blance 
#             2 == withdraw blance
            
#             3 == deposit blance
#             4 == exit
            
#             """)
#     try:
#         option = int(input("please enter your choice"))
#     except:
#       print("please enter valid option ")
#     if option == 1:
#         print(f"Your current blance is {blance}")



#     if option == 2:
#         withdraw_amount = int(input("please enter withdraw_amount "))
#         balance = balance - withdraw_amount
#         print(f"{withdraw_amount} is debited from your accpunt ")
#         print(f"your updated balance is {balance}")

#     if option == 3:
#         deposite_amount  = int(input("please enter deposite_amount"))
#         balance = balance + deposite_amount 
#         print(f"{deposite_amount} is credited to your account")
#         print(f"your updated balance is {balance}")


#     if option == 4:
#         print("Thanks for using this atm")
#     else:
#         print("Envali this atm")
#         break    


        
# else:
#     print("Wrong pin please try again")

125



import time

print("Please insert your Card")
time.sleep(5)
password = 1234
balance = 5000  # Initial balance
pin = int(input("Enter your ATM pin: "))

if pin == password:
    while True:
        print("""
            1 == Balance 
            2 == Withdraw balance
            3 == Deposit balance
            4 == Exit
            """)
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue
        
        if option == 1:
            print(f"Your current balance is {balance}")
        
        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter withdraw amount: "))
                if withdraw_amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"Your updated balance is {balance}")
            except ValueError:
                print("Please enter a valid amount.")
        
        elif option == 3:
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account")
                print(f"Your updated balance is {balance}")
            except ValueError:
                print("Please enter a valid amount.")
        
        elif option == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")
else:
    print("Wrong pin, please try again.")
