# COMP90024     Group 66
# Ziyang Zhang 	1139552
# Yanjun Ma     1184516
# Tianyi Zheng 	1024493
# Yining Ding 	874213
# Zixin Zhang 	1087336
# Description   This document is used to save the crime data from abs.gov.au to the database in CouchDB

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
