# import couchdb
# import json
# couch = couchdb.Server('http://admin:password@172.26.132.125:5555/')
#
# try:
#     database = couch['aurin']
# except:
#     couch.create('aurin')
#     db = couch['aurin']
#
# with open(<your file name>) as jsonfile:
#     for row in jsonfile:
#         json_entry = json.load(row)
#         db.save(json_entry)


import ujson
import re

properties = []
mental_health = []
result = {}

with open('data2759703005553866823.json', 'rb') as f:
    data = ujson.load(f)
for i in data['features']:
    properties.append(i["properties"]["sa3_name"])
    mental_health.append(i["properties"]['mentalhlth_rel_pres_tot'])


def combined(city):
    cnt = 0
    for i in range(len(properties)):
        if re.search(r'(?i)'+city+'', properties[i]):
            cnt += 1
            key = city
            if key in result.keys():
                result[key] += mental_health[i]
            else:
                result.update({key: mental_health[i]})


combined('Sydney')
combined('Melbourne')
combined('Brisbane')
combined('Perth')
combined('Adelaide')
combined('Gold Coast')
combined('Newcastle')
print(result)

# {'Sydney': 4020, 'Melbourne': 1509, 'Brisbane': 3654, 'Perth': 2398, 'Adelaide': 3145, 'Gold Coast': 1157, 'Newcastle': 2307}

# try:
#     database = couch['aurin_mental']
# except:
#     couch.create('aurin_mental')
#     db = couch['aurin_mental']
#
# for k, v in result.items():
#     db.save({"location": k, "mental_health": v})


