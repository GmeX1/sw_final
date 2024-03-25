import requests as req
import json
import datetime

with open('light.json') as f:
    data = json.load(f)
galaxy_type = input()
date = datetime.datetime.strptime(input(), '%Y/%m/%d').date()

server_data = eval(req.get(f'http://{data["host"]}:{data["port"]}').text)
out = set()
for key in server_data.keys():
    if datetime.datetime.strptime(key, '%Y/%m/%d').date() < date:
        for item in server_data[key]:
            if item['type'] == galaxy_type:
                out.add(item['galaxy'])
print(', '.join(sorted(out)))
