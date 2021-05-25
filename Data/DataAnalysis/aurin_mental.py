# COMP90024     Group 66
# Ziyang Zhang 	1139552
# Yanjun Ma     1184516
# Tianyi Zheng 	1024493
# Yining Ding 	874213
# Zixin Zhang 	1087336
# Description   This document is used to save the mental health data from aurin to the database in CouchDB

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

