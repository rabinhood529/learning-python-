# def calculate_total(price,tax_rate):
#   total=price + (price * tax_rate)
#   return total

# print(calculate_total(25,0.05))
# print(calculate_total(26,0.04))

# Lesson 10: Logic & Functions (The "Guard" Pattern)
def verify_login(input_password,correct_password):
  if len(input_password)<5:
    return f"Password too short"
  elif input_password==correct_password:
    return f"Acess Granted"
  else:
    return f"Acess Denied"
  

