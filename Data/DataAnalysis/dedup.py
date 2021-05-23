import pandas as pd
import couchdb

couch = couchdb.Server('http://admin:password@172.26.130.232:5984/')

database = couch['twitter']

try:
    database1 = couch['unique_twitter']
except:
    couch.create('unique_twitter')
    database1 = couch['unique_twitter']

try:
    database2 = couch['last_refresh_amount_record']
except:
    couch.create('last_refresh_amount_record')
    database2 = couch['last_refresh_amount_record']
    database2.save({"amount": 0})

data = {"selector": {},
        "fields": ['amount'],
        "limit": database2.__len__()
        }
for items in database2.find(data):
    previous_amount = items['amount']

present_amount = database.__len__()
for id in database2:
    database2.delete(database2[id])
database2.save({"amount": present_amount})

lines = database.view('_all_docs', include_docs=True, descending=True, limit=present_amount-previous_amount)
data = [line['doc'] for line in lines]

dataframe = pd.DataFrame(data)
dataframe.drop_duplicates(subset='id', inplace=True)
dict = dataframe.to_dict('records')

for l in dict:
    database1.save({"id": l['id'], "text": l['text'], 'coordinates': l['coordinates'], "location": l['location'],
                   "language": l['language'], "friends_count": l['friends_count']})

