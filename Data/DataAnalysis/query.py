import couchdb
import re
from textblob import TextBlob

# couch = couchdb.Server('http://admin:password@172.26.132.232:5984/')
couch = couchdb.Server('http://admin:password@172.26.130.232:5984//')
database = couch['dedup_twitter']

try:
    couch.create('covid19_test')
except:
    couch.delete('covid19_test')
    couch.create('covid19_test')

database2 = couch['covid19_test']

try:
    couch.create('crime_test')
except:
    couch.delete('crime_test')
    couch.create('crime_test')

database3 = couch['crime_test']

data = {"selector": {},
        "fields": ['id', "text", "coordinates", "location", "language", "friends_count"],
        "limit": database.__len__()
        }

for items in database.find(data):
    blob = TextBlob(items['text'])
    score = blob.sentiment
    subjectivity = score.subjectivity
    polarity = score.polarity
    if polarity == 0:
        continue
    else:
        isPos = -1 if polarity < 0 else 1
        word1=re.search(
                r'(?i)Coronavirus|covid|quarantine|Anosmia|Antibodies|Antibody|Bacteria|Cardiovascular|Cohort|Comorbidity|Conjunctivitis|virus|Cure|Dysgeusia|Epidemic|Epidemiologists|Herd immunity|Hygiene|Immunity|Incidence|Kawasaki disease|Morbidity|Mortality|Myalgia|Pandemic|Physical distancing|Plasma|Prevalence|SARS|Self-isolation|Serology|Treatment|Vaccine',
                items["text"])
        word2=re.search(
                r'(?i)homicide|sexual assault|kidnap|abduction|robbery|blackmail|extortion|theft|unlawful|murder|manslaughter|crime|victim|security|criminal|criminology|abduction|arson|assassin|assault|assailant|bigamy|bigamist|bombing|bomber|bribery|briber|burglary|burglar|abuse|corruption|criminal|cybercrime|violence|drunk driving|drunk driver|embezzlement|embezzler|espionage|spy|forgery|forger|fraud|genocide|hijack|hit and run|hooligan|libel|loot|lynching|mugger|mugging|perjury|pickpocket|pilfering|poach|rape|riot|shoplift|slander|smuggl|speeding|terroris|thief|traffick|treason|traitor|trespass|vandal|voyeur'
                , items["text"])
        if word1:
            database2.save({"id": items["id"], "text": items["text"], 'coordinates': items["coordinates"],
                            "location": items["location"], "language": items["language"],
                            "friends_count": items["friends_count"], "polarity": polarity, "isPos": isPos,"word":word1.group().lower()})

        if word2:
            database3.save({"id": items["id"], "text": items["text"], 'coordinates': items["coordinates"],
                            "location": items["location"], "language": items["language"],
                            "friends_count": items["friends_count"], "polarity": polarity, "isPos": isPos,"word":word2.group().lower()})


    # if polarity <= 0:
    #     database4.save({"id": items["id"], "text": items["text"], 'coordinates': items["coordinates"],
    #                     "location": items["location"], "language": items["language"],
    #                     "friends_count": items["friends_count"], "polarity": polarity})


# happy:       2515     covid: 42    crime: 26
# <= 0 (4508): 5458 (-299.7310813520969)    covid: 66 (-4.0777777777777775)   crime: 66 (-5.664186507936508)
# negative:    950      covid: 11    crime: 12
# total_twit:  7973     covid: 108   crime: 92
