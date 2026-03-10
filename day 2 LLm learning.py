# # formatting string like %i and %s and learning about type casting
# raw_price = "45"
# tax = 5
# total_price = int(raw_price)+tax
# # print(f"{total_price}")

# raw_price="45"
# tax=5
# total_price=int(raw_price)+tax
# print("Final Database Entry:%i" % total_price)

# print("the raw price is %s and tax is %i now total_price is:",total_price)


# # learning list
# exercise 1
# cart_prices = [ " 10 " , " 20 " , " 30 " ]
# cart_prices[2] = 25
# print(cart_prices)
#exercise 2

# raw_prices = [" 10 ", " 20 ", " 30 "]

# clean_prices = []

# for prices in raw_prices:
#   cleaned=int(prices.strip())
#   clean_prices.append(cleaned)

#   print(clean_prices)


  # dictionary 
# user_db = { "Rohit" : "rohit123@gmail.com",
#              "tray" : "tre123@gmail.com",
#              "sohit" :"sohit456@gmail.com"
#              }

# user_db["Rohit"] = "new_Rohit@bank.com"
# if "Rohit" in user_db:
#   print("User list found")
# else:
#   print("User not found")


# print("Database State: {}".format(user_db))


sender = "Alice"
receiver = "Bob"
amount = 100
print("TRABSFER: %s sent %i dollars to %s" % (sender ,amount , receiver))
print("TRABSFER: {} sent {} dollars to {}".format(sender,amount,receiver))
