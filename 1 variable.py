item_name="Milk"
quantity=3
price_per_unit=2.5
subtotal=quantity*price_per_unit
tax_rate=0.08
tax_amount=subtotal* tax_rate
total_bill=subtotal+tax_amount
print(f"Customer bought 3 units of Milk. Total bill is: ${ total_bill}") #here instead of 3 use {quanity} and of milk use {item_name}? why ?
#because there is change we dont have to reqiere and program shoule be dyanmic
