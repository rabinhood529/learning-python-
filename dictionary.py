# profile={
# "username":"host",
# "level":10,
# "is_active":True
# }

# profile["level"]+=1
# profile["is_active"]=False
# profile["last_login"]="Monday"
# print(profile)

# The "Real World" Challenge: The Server Status Checker


servers=[
{"name": "Web-01", "status": "Active"},

{"name": "Auth-01", "status": "Down"},

{"name": "DB-01", "status": "Active"}


]

for server in servers:
  if server["status"].lower()=="down":
    print(f"Alert:{server['name']} is down")