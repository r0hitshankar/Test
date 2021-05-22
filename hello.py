import datetime
today = datetime.datetime.now()
print("Monitor Python file")
print(today.strftime("%d-%b %H Hr"))
import requests

str2="https://stackoverflow.com"
r = requests.head(str2)
print(str(str2)+":"+str(r.status_code))
