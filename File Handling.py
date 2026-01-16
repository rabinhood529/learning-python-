def log_error(server_name):
  with open("server_logs.txt","a") as file:
    file.write(f"{server_name} is DOWN! \n")

    print(log_error("Web=01"))
    print(log_error("Database-X"))