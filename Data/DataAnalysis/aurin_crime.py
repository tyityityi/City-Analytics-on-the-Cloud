import pandas as pd
data=pd.read_excel('tmpB2ZP9eAFP---Crime-incidents-data.xls')
column=data[4:5]
data=data[5:]
data.loc['Row_sum'] = data.apply(lambda x: x.sum())
result={}
#print(column.iloc[0][2:-1])

# print(data.loc['Row_sum'][2:-1])
column=column.iloc[0][2:-1]
cnt=data.loc['Row_sum'][2:-1]
for i in range(len(column)):
    result.update({column[i]: cnt[i]})

print(result)