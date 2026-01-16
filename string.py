raw_name=" jhon DoE "
space=raw_name.strip()
case=raw_name.upper()
correct_name=case
password = "Secret123"
length=(len(password))
if len(password)<8:
  print("Warning ! password must be 8 character")
else:
  print(f"User{correct_name} has registered with a {length}-character password.")