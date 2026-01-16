servers=[
  {"name": "Web-01", "status": "Active"},

{"name": "Auth-01", "status": "Down"},

{"name": "DB-01", "status": "Active"}
]

def save_log(server_name):
    try:
          with open("ncident_reports.txt","a") as file:
              file.write(f"Server is down{server_name}is down!\n")
          except PermissionError:
print("Error:could not write to file")

        
        


def check_status():

  for server in servers:
      if server["status"].lower=="down":
          save_log(server["name"])

        check_status()


    