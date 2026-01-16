balance=1000
deposit_amount=0
withdraw_amount=0
Check_Balance=0
count=0
fees=2
while count<3:
  pin=int(input("enter 4 digit pin:"))
  if pin==1234:
    print("access granted:")
    break

  else: 
    count+=1
    print(f"Wrong. Attempts left: {3 - count}")


  if count==3:
    print("Card blocked:")
    exit()

  else:
    print("menu:")

  while True:
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
   
enter=int(input("enter a number:"))
  
  

if enter==1:
      Check_Balance=balance
      print(f"your balance is {Check_Balance}")
  
elif enter==2:
  deposit_amount=int(input("enter amount to be deposited in value:"))
  if deposit_amount<=0:
    print("Invalid amount:")
  else:
    print(f"deposit amount:{deposit_amount}")

elif enter==3:
    withdraw_amount=int(input("enter amount to withdraw:"))
    total_cost=withdraw_amount+fees


    if withdraw_amount>=balance:
      print("insuffceint money")
      
    elif withdraw_amount<=0:
      print("invalid amount:")
    else:
      balance=balance-total_cost
      printf(f"successs!withdraw:{withdraw_amount}.FEE:$2")
      print(f"new balance:${balance}")

elif enter==4:
  print("Exiting...")
  
else:
        print("Invalid option. Please choose 1-4.")



  