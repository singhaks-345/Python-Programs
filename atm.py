import time
print("***** Please Insert your Card *****")
time.sleep(5)
password=1234
pin=int(input("Enter Your Pin:"))
balance=5000
if pin==password:
  while  True:
    print("......Chose an option......")
    print ("""
    1 : balance
    2 : Withdraw Balance
    3 : Deposit Balance
    4 : exit
                
    """)
    try:
        option=int(input("Please Enter your Choise:"))
    except:
        print("Please Enter Valid Option !")
    if option==1:
        print(f"Your Current Balance is: {balance} !")
    if option==2:
        Withdraw_amount=int(input("Please Enter Withdraw_amount :"))
        balance=balance-Withdraw_amount
        print(f"{Withdraw_amount} is debited from your account :")
        print(f"Your updated Balance is : {balance}")
    if option==3:
        deposit_amount=int(input("Please Enter deposit_amount:"))
        balance=balance+deposit_amount
        print(f"{deposit_amount} is credited to your account !") 
        print(f"your updated balance is :{balance} !")
    if option==4:
        break               
            
else:
    print("Wrong Pin ,Please try Again !")