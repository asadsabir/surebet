import requests
import datetime as dt
from auth import * 

date = dt.datetime.now().date()
pl_url = f"https://api.soccersapi.com/v2.2/fixtures/?user={SOCCER_USERNAME}&token={SOCCER_TOKEN}&t=schedule&d={date}&league_id=1134"

payload={}
headers = {}

response = requests.request("GET", pl_url, headers=headers, data=payload)

print(response)