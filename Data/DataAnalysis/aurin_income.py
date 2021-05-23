import ujson, re

properties = []
employment = []
income = []
result = {}

with open('data7759631866113944748.json', 'rb') as f:
    data = ujson.load(f)
for i in data['features']:
    properties.append(i["properties"]["sa4_name16"])
    employment.append(i["properties"]['p_2017_18_employed_persons_000'])
    income.append(i["properties"]['p_2017_18_median_employment_income_per_employed_person_aud'])


def combined(city):
    cnt = 0
    for i in range(len(properties)):
        if re.search(r'(?i)'+city+'', properties[i]):
            cnt += 1
            key = city
            if key in result.keys():
                result[key] = [result[key][0] + employment[i], result[key][1]+income[i]]
            else:
                result.update({key: [employment[i], income[i]]})
    result[key] = [round(result[key][0],2), result[key][1]/cnt]



combined('Sydney')
combined('Melbourne')
combined('Brisbane')
combined('Perth')
combined('Adelaide')
combined('Gold Coast')
combined('Newcastle')
print(result)
