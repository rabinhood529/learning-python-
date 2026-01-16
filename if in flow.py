Stock=["Laptop", "Mouse", "Keyboard", "Monitor"]
buy=input("enter the device you want to buy:").strip().title()
if buy in Stock:
  print("Item availale")
  Stock.remove(buy)
  print(Stock)
else:
  print("Sorry,we are out of stock")
