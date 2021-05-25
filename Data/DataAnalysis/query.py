# COMP90024     Group 66
# Yanjun Ma     1184516
# Yining Ding 	874213
# Zixin Zhang 	1087336
# Ziyang Zhang 	1139552
# Tianyi Zheng 	1024493
# Description   This document extracts unique tweets which are related with Covid19 or Crime and save them into two different database 


import couchdb
import re
from textblob import TextBlob

couch = couchdb.Server('http://admin:password@172.26.130.232:5984/')
database = couch['unique_twitter']

try:
    database2 = couch['covid19_related']
except:
    couch.create('covid19_related')
    database2 = couch['covid19_related']

try:
    database3 = couch['crime_related']
except:
    couch.create('crime_related')
    database3 = couch['crime_related']


database4 = couch['last_unique_amount_record']
data1 = {"selector": {},
         "fields": ['amount'],
         "limit": database4.__len__()
         }
for items in database4.find(data1):
    previous_amount = items['amount']

present_amount = database.__len__()

lines = database.view('_all_docs', include_docs=True, descending=True, limit=present_amount - previous_amount)
data = [line['doc'] for line in lines]

for items in data:
    blob = TextBlob(items['text'])
    score = blob.sentiment
    subjectivity = score.subjectivity
    polarity = score.polarity
    if polarity == 0:
        continue
    else:
        isPos = -1 if polarity < 0 else 1
        word1 = re.search(
            r'(?i)Coronavirus|covid|quarantine|Anosmia|Antibodies|Antibody|Bacteria|Cardiovascular|Cohort|Comorbidity|Conjunctivitis|virus|Cure|Dysgeusia|Epidemic|Epidemiologists|Herd immunity|Hygiene|Immunity|Incidence|Kawasaki disease|Morbidity|Mortality|Myalgia|Pandemic|Physical distancing|Plasma|Prevalence|SARS|Self-isolation|Serology|Treatment|Vaccine',
            items["text"])
        word2 = re.search(
            r'(?i)homicide|sexual assault|kidnap|abduction|robbery|blackmail|extortion|theft|unlawful|murder|manslaughter|crime|victim|security|criminal|criminology|abduction|arson|assassin|assault|assailant|bigamy|bigamist|bombing|bomber|bribery|briber|burglary|burglar|abuse|corruption|criminal|cybercrime|violence|drunk driving|drunk driver|embezzlement|embezzler|espionage|spy|forgery|forger|fraud|genocide|hijack|hit and run|hooligan|libel|loot|lynching|mugger|mugging|perjury|pickpocket|pilfering|poach|rape|riot|shoplift|slander|smuggl|speeding|terroris|thief|traffick|treason|traitor|trespass|vandal|voyeur'
            , items["text"])
        if word1:
            database2.save({"id": items["id"], "text": items["text"], 'coordinates': items["coordinates"],
                            "location": items["location"], "language": items["language"],
                            "friends_count": items["friends_count"], "polarity": polarity, "isPos": isPos,
                            "word": word1.group().lower()})

        if word2:
            database3.save({"id": items["id"], "text": items["text"], 'coordinates': items["coordinates"],
                            "location": items["location"], "language": items["language"],
                            "friends_count": items["friends_count"], "polarity": polarity, "isPos": isPos,
                            "word": word2.group().lower()})
