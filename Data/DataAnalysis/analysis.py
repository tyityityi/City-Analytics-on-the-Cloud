import pandas as pd
import couchdb

# couch = couchdb.Server('http://admin:password@172.26.132.232:5984/')
couch = couchdb.Server('http://admin:password@172.26.130.232:5984/')
database = couch['covid19_test']
database1 = couch['crime_test']
# database2 = couch['unhappy_twitter']

# covid analysis
lines = database.view('_all_docs', include_docs=True)
cov_data = [line['doc'] for line in lines]
df = pd.DataFrame(cov_data)
df1 = df.groupby(['isPos','language','location']).aggregate({'polarity': 'sum'})
df1['count'] = df.groupby(['isPos','language','location']).count()['_id']
df1['percent'] = df1['polarity']/df1['count']

dict = df1.to_dict('index')
print(dict)
d = {1: [], -1: []}
for k in dict.keys():
    dict[k].update({"lang": k[1], "loc": k[2]})
    if k[0] == 1:
        d[1].append(list(dict[k].values()))
    else:
        d[-1].append(list(dict[k].values()))
try:
    couch.create('covid_anay')
except:
    couch.delete('covid_anay')
    couch.create('covid_anay')
database2 = couch['covid_anay']
database2.save(d)

# 前端代码
# for k in dict.keys():
#     if k[0] == 1:
#         dict[k].update({"lang":k[1], "loc":k[2]})
#         print(dict[k])



# crime analysis
lines1 = database1.view('_all_docs', include_docs=True)
crime_data = [line['doc'] for line in lines1]
df2 = pd.DataFrame(crime_data)
df3 = df2.groupby(['isPos','language','location']).aggregate({'polarity': 'sum'})
df3['count'] = df2.groupby(['isPos','language','location']).count()['_id']
df3['percent'] = df3['polarity']/df3['count']

dict2 = df3.to_dict('index')
d2 = {1: [], -1: []}
for k in dict2.keys():
    dict2[k].update({"lang": k[1], "loc": k[2]})
    if k[0] == 1:
        d2[1].append(list(dict2[k].values()))
    else:
        d2[-1].append(list(dict2[k].values()))
try:
    couch.create('crime_anay')
except:
    couch.delete('crime_anay')
    couch.create('crime_anay')
database3 = couch['crime_anay']
database3.save(d2)

# covid: friends count vs polarity
df4 = df[['location', 'friends_count', 'polarity']][1:]
dict_cofvp = df4.to_dict('records')
dicCo = {}
for k in dict_cofvp:
    if dicCo.get(k['location']):
        dicCo[k['location']].append([k['friends_count'], k['polarity']])
    else:
        dicCo[k['location']] = [[k['friends_count'], k['polarity']]]

try:
    couch.create('cov_friends_vs_polarity')
except:
    couch.delete('cov_friends_vs_polarity')
    couch.create('cov_friends_vs_polarity')
database4 = couch['cov_friends_vs_polarity']
database4.save(dicCo)

# crime: friends count vs polarity
df5 = df2[['location', 'friends_count', 'polarity']][1:]
dict_crfvp = df5.to_dict('records')
dictCr = {}
for k in dict_crfvp:
    if dictCr.get(k['location']):
        dictCr[k['location']].append([k['friends_count'], k['polarity']])
    else:
        dictCr[k['location']] = [[k['friends_count'], k['polarity']]]

try:
    couch.create('crime_friends_vs_polarity')
except:
    couch.delete('crime_friends_vs_polarity')
    couch.create('crime_friends_vs_polarity')
database5 = couch['crime_friends_vs_polarity']
database5.save(dictCr)


# df = dataframe[['location', 'polarity']]
# df1 = df.groupby(df['location']).aggregate({'polarity': 'sum'})
# df1['count'] = df.groupby(df['location']).count()
# print(df1)
#
# Total = df1['polarity'].sum()
# print(Total)


# lines = database1.view('_all_docs', include_docs=True)
# cri_data = [line['doc'] for line in lines]
# dataframe2 = pd.DataFrame(cri_data)
# df2 = dataframe2[['location', 'polarity']]
# df3 = df2.groupby(df2['location']).aggregate({'polarity': 'sum'})
# df3['count'] = df2.groupby(df2['location']).count()
# print(df3)
#
# Total = df3['polarity'].sum()
# print(Total)


# lines = database2.view('_all_docs', include_docs=True)
# neg_data = [line['doc'] for line in lines]
# dataframe3 = pd.DataFrame(neg_data)
# df4 = dataframe3[['location', 'polarity']]
# df5 = df4.groupby(df4['location']).aggregate({'polarity': 'sum'})
# df5['count'] = df4.groupby(df4['location']).count()
# print(df5)
#
# Total = df5['polarity'].sum()
# print(Total)


# dict = df5.to_dict('index')
# print(dict)
#
# database3 = couch['test']
# database3.save(dict)
# for l in dict:
#     print(l)
#     # database3.save({"polarity": l['id'], "count": l['count']})
