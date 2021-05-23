from flask import Flask, render_template, jsonify
import simplejson
from flask import Flask, g, request
import os
# os.system("python map1.py")

from couchdb.design import ViewDefinition
import couchdb
import subprocess
import json

from jinja2 import Markup
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Geo
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url
from pyecharts import options as opts
from pyecharts.charts import Gauge
from pyecharts.charts import Radar
from pyecharts.charts import Grid, Liquid
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

user = "admin"
password = "password"
couchserver = couchdb.Server("http://%s:%s@172.26.132.125:5555/" % (user, password))
#
# # for dbname in couchserver:
# # print(dbname)
#
dbname1 = "cov_friends_vs_polarity"
dbname2 = "crime_friends_vs_polarity"
dbname3 = "covid_anay"
dbname4 = "crime_anay"
dbname5 = "aurin_employincome"
dbname6 = "aurin_mental"

if dbname1 in couchserver:
    db1 = couchserver[dbname1]
# else:
#     db1 = couchserver.create(dbname1)

if dbname2 in couchserver:
    db2 = couchserver[dbname2]

if dbname3 in couchserver:
    db3 = couchserver[dbname3]

if dbname4 in couchserver:
    db4 = couchserver[dbname4]

if dbname5 in couchserver:
    db5 = couchserver[dbname5]

if dbname6 in couchserver:
    db6 = couchserver[dbname6]
#
# # doc_id = "created:dedup_twitter"
# # doc = db[doc_id]
# # print(doc)
#
#

list1 = []
covid_fc = []
covid_p = []

crime_fc = []
crime_p = []

co_pos_lan = []
co_neg_lan = []
cr_pos_lan = []
cr_neg_lan = []

for item in db3.view('_design/newdoc3/_view/new-view', include_docs=True):
    temp3 = item.doc
    # print(temp3)
    for j in temp3:
        if j == '1':
            for k in range(0, len(temp3[j])):
                co_pos_lan.append(temp3[j][k][3])
        if j == '-1':
            for k in range(0, len(temp3[j])):
                co_neg_lan.append(temp3[j][k][3])
appear1 = []
appear2 = []
for item in co_pos_lan:
    appear1.append(co_pos_lan.count(item) / len(co_pos_lan) * 100)
for item in co_neg_lan:
    appear2.append(co_neg_lan.count(item) / len(co_neg_lan) * 100)


def unique(old_list):
    newList = []
    for x in old_list:
        if x not in newList:
            newList.append(x)
    return newList


finalcopl = unique(co_pos_lan)
finalconl = unique(co_neg_lan)

finalcopv = unique(appear1)
finalconv = unique(appear2)

# print(appear1)
# print(appear2)
# print(co_pos_lan)
# print(co_neg_lan)
# print(finalcopl)
# print(finalcopv)
#
# print(finalconl)
# print(finalconv)


for item in db4.view('_design/newdoc4/_view/new-view', include_docs=True):
    temp4 = item.doc
    for j in temp4:
        if j == '1':
            for k in range(0, len(temp4[j])):
                cr_pos_lan.append(temp4[j][k][3])
        if j == '-1':
            for k in range(0, len(temp4[j])):
                cr_neg_lan.append(temp4[j][k][3])
appear3 = []
appear4 = []
for item in cr_pos_lan:
    appear3.append(cr_pos_lan.count(item) / len(cr_pos_lan) * 100)
for item in cr_neg_lan:
    appear4.append(cr_neg_lan.count(item) / len(cr_neg_lan) * 100)

finalcrpl = unique(cr_pos_lan)
finalcrnl = unique(cr_neg_lan)

finalcrpv = unique(appear3)
finalcrnv = unique(appear4)

# print(finalcrpl)
# print(finalcrnl)
# print(finalcrpv)
# print(finalcrnv)


city_name = []
employ = []
income = []
for item in db5.view('_design/employincome/_view/new-view', include_docs=True):
    temp5 = item.doc
    # print(temp5)
    for j in temp5:
        if j != '_id' and j != '_rev':
            city_name.append(j)
            employ.append(temp5[j][0])
            income.append(temp5[j][1])

employk = []
for item in employ:
    employk.append(item / 1000)

incomek = []
for item in income:
    incomek.append(item / 1000)

#print(city_name)
# print(employ)
# print(income)
city_co_p = []
city_co_n = []
city_cr_p = []
city_cr_n = []

for item in db3.view('_design/newdoc3/_view/new-view', include_docs=True):
    temp31 = item.doc
    # print(temp31)
    for j in temp31:
        if j == '1':
            for k in range(0, len(temp31[j])):
                if temp31[j][k][4] in city_name or temp31[j][k][4] == "Perth (WA)":
                    city_co_p.append([temp31[j][k][4], temp31[j][k][0]])
        if j == '-1':
            for k in range(0, len(temp31[j])):
                if temp31[j][k][4] in city_name or temp31[j][k][4] == "Perth (WA)":
                    city_co_n.append([temp31[j][k][4], temp31[j][k][0]])

# print(city_co_p)
# print(city_co_n)

city_co_pc = []
city_co_nc = []
city_co_allc = []

city_cr_pc = []
city_cr_nc = []

for item in db3.view('_design/newdoc3/_view/new-view', include_docs=True):
    temp32 = item.doc
    # print(temp31)
    for j in temp32:
        if j == '1':
            for k in range(0, len(temp32[j])):
                if temp32[j][k][4] in city_name or temp32[j][k][4] == "Perth (WA)":
                    city_co_pc.append([temp32[j][k][4], temp32[j][k][1]])
        if j == '-1':
            for k in range(0, len(temp32[j])):
                if temp32[j][k][4] in city_name or temp32[j][k][4] == "Perth (WA)":
                    city_co_nc.append([temp32[j][k][4], temp32[j][k][1]])
# print(city_co_pc)
# print(city_co_nc)


arr_pc = []
arr_nc = []


def arrangelist(old_list):
    newList = []
    for k in range(0, len(old_list)):
        for item in old_list:
            if item[0] == city_name[k]:
                newList.append(item[1])
    return newList


# for k in range(0, len(city_co_pc)):
#     for item in city_co_pc:
#         if item[0] ==city_name[k]:
#             arr_pc.append(item[1])
arr_pc = arrangelist(city_co_pc)
arr_pc.insert(3, city_co_pc[5][1])

arr_nc = arrangelist(city_co_nc)
arr_nc.insert(3, city_co_nc[5][1])

# print(arr_pc)
# print(arr_nc)

city_co_allc = [arr_pc[i]+arr_nc[i] for i in range(min(len(arr_pc),len(arr_nc)))]
# print(city_co_allc)









city_cr_pc = []
city_cr_nc = []

for item in db4.view('_design/newdoc4/_view/new-view', include_docs=True):
    temp42 = item.doc
    # print(temp31)
    for j in temp42:
        if j == '1':
            for k in range(0, len(temp42[j])):
                if temp42[j][k][4] in city_name or temp42[j][k][4] == "Perth (WA)":
                    city_cr_pc.append([temp42[j][k][4], temp42[j][k][1]])
        if j == '-1':
            for k in range(0, len(temp42[j])):
                if temp42[j][k][4] in city_name or temp42[j][k][4] == "Perth (WA)":
                    city_cr_nc.append([temp42[j][k][4], temp42[j][k][1]])
# print(city_cr_pc)
# print(city_cr_nc)


arr_pc_r = []
arr_nc_r = []

arr_pc_r = arrangelist(city_cr_pc)
arr_pc_r.insert(3, city_cr_pc[5][1])

arr_nc_r = arrangelist(city_cr_nc)
arr_nc_r.insert(3, city_cr_nc[5][1])

# print(arr_pc_r)
# print(arr_nc_r)

city_cr_allc = [arr_pc_r[i]+arr_nc_r[i] for i in range(min(len(arr_pc_r),len(arr_nc_r)))]
# print(city_cr_allc)

















for item in db4.view('_design/newdoc4/_view/new-view', include_docs=True):
    temp41 = item.doc
    # print(temp31)
    for j in temp41:
        if j == '1':
            for k in range(0, len(temp41[j])):
                if temp41[j][k][4] in city_name or temp41[j][k][4] == "Perth (WA)":
                    city_cr_p.append([temp41[j][k][4], temp41[j][k][0]])
        if j == '-1':
            for k in range(0, len(temp41[j])):
                if temp41[j][k][4] in city_name or temp41[j][k][4] == "Perth (WA)":
                    city_cr_n.append([temp41[j][k][4], temp41[j][k][0]])

#
# print(city_cr_p)
# print(city_cr_n)

arrange1 = []
arrange2 = []
arrange3 = []
arrange4 = []

# print(city_co_p)
for k in range(0, len(city_co_p)):
    for item in city_co_p:
        if item[0] == city_name[k]:
            arrange1.append(item[1])

arrange1.insert(3, city_co_p[5][1])

for k in range(0, len(city_co_n)):
    for item in city_co_n:
        if item[0] == city_name[k]:
            arrange2.append(item[1])
arrange2.insert(3, city_co_n[5][1])

for k in range(0, len(city_cr_p)):
    for item in city_cr_p:
        if item[0] == city_name[k]:
            arrange3.append(item[1])
arrange3.insert(3, city_cr_p[5][1])

for k in range(0, len(city_cr_n)):
    for item in city_cr_n:
        if item[0] == city_name[k]:
            arrange4.append(item[1])
arrange4.insert(3, city_cr_n[5][1])
# print(arrange1)
# print(arrange2)
# print(arrange3)
# print(arrange4)

# finalcrpl=unique(cr_pos_lan)
# finalcrnl=unique(cr_neg_lan)
#
# finalcrpv=unique(appear3)
# finalcrnv=unique(appear4)
# for item in db.view('_design/newdoc/_view/new-view', include_docs=True):
#     temp = item.doc
#     print(dir(temp))
#     print(type(temp))
#     print(temp['Ballarat'])
#     list1.append(temp['Ballarat'][0][0])
#     # data = temp.__dict__
#     # print(jsonify(data))

for item in db1.view('_design/cofp/_view/new-view', include_docs=True):
    temp = item.doc
    for j in temp:
        if j != '_id' and j != '_rev':
            for k in range(0, len(temp[j])):
                covid_fc.append(temp[j][k][0])
                covid_p.append(temp[j][k][1])
# print(covid_fc)
# print(covid_p)

for item in db2.view('_design/crfp/_view/new-view', include_docs=True):
    temp2 = item.doc
    for j in temp2:
        if j != '_id' and j != '_rev':
            for k in range(0, len(temp2[j])):
                crime_fc.append(temp2[j][k][0])
                crime_p.append(temp2[j][k][1])

# print(crime_fc)
# print(crime_p)


mental = []
for item in db6.view('_design/aurin_mental/_view/new-view', include_docs=True):
    temp6 = item.doc
    # print(temp6)
    for j in temp6:
        if j != '_id' and j != '_rev':
            mental.append(temp6[j])

# print(mental)


# curl http://admin:password@172.26.132.232:5984/_global_changes/_all_docs
# curl "http://admin:password@172.26.132.232:5984/_global_changes/_all_docs?include_docs=true&key=\"created:dedup_twit
# ter\"

# docs_by_author = ViewDefinition('docs', 'byauthor',
#                                 'function(doc) { emit(doc.author, doc);}')

cowordcount = []
crwordcount = []

cosubprocess = subprocess.getoutput(
    "curl http://admin:password@172.26.132.125:5555/covid19_test/_design/test/_view/test?group=true")
rows = cosubprocess.split('[')[1].split(']')[0]
j = json.loads("[" + rows + "]")
for i in j:
    cowordcount.append([i['key'], i['value']])

# print(cowordcount)

crsubprocess = subprocess.getoutput(
    "curl http://admin:password@172.26.132.125:5555/crime_test/_design/crimetest/_view/crimetest?group=true")
rows2 = crsubprocess.split('[')[1].split(']')[0]
j2 = json.loads("[" + rows2 + "]")
for i in j2:
    crwordcount.append([i['key'], i['value']])

# print(crwordcount)
