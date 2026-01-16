def safe_divide(total_bonus,number_of_employees):
  try:
    Bonus=total_bonus/number_of_employees

  except ZeroDivisionError:
    return f"Error:Cannot divide by zero employees"
  
  print(safe_divide(1000,5))
  print(safe_divide(1000,0))
