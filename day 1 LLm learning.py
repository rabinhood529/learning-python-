# # Checking server 
# status = True
# print(status)


# is_power_on = True
# is_internet_connected = True

# if is_power_on == True and is_internet_connected == True:
#   server_status = True
#   print(server_status)


is_main_power_on = False
is_backup_generator_on = True
is_internet_connected = True
is_server_overheating = True
server_status = (is_main_power_on or is_backup_generator_on) and is_internet_connected and (not is_server_overheating)

print(server_status)

 
