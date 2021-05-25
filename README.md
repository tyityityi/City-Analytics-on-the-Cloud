# **City Analytics on the Cloud**
## **Cluster and Cloud Computing 2021 Assignment 2 - Team 66**
This repository contains the source code for assignment 2 of the COMP90024 Cluster and Cloud Computing course at the University of Melbourne.

## **Contributors**

- Tianyi Zheng 	1024493
- Zixin Zhang 	1087336
- Ziyang Zhang 	1139552
- Yanjun Ma 	1184516
- Yining Ding 	874213

The system architecture designed for this project is deployed on the [University of Melbourne Research Cloud](https://dashboard.cloud.unimelb.edu.au/). It makes use of various technologies such as [Ansible](https://www.ansible.com), [Docker](https://www.docker.com) and [Apache CouchDB](https://couchdb.apache.org). 

The data used to analysis is retrieved from [Aurin](https://aurin.org.au/) and [Twitter API](https://developer.twitter.com/en/docs/twitter-api)

## **Webpage** 

[http://172.26.128.188/](http://172.26.128.188/) 

(requires active connection Unimelb Cisco VPN)

## **YouTube Link**

System architecture and delpoyment: [https://youtu.be/CLgQxwq6uDI](https://youtu.be/CLgQxwq6uDI)

Scenarios and Demo:[https://youtu.be/hJKhXxit9uc](https://youtu.be/hJKhXxit9uc)


## **CouchDB Cluster Adminstration Page**
Master Node: [172.26.130.232/5984/_utils](172.26.130.232/5984/_utils)

Sub Node 1: [172.26.128.156/5984/_utils](172.26.128.156/5984/_utils)

Sub Node 2: [172.26.131.18/5984/_utils](172.26.131.18/5984/_utils)

## **Project Structure**
```
  /Ansible
      - ansible scripts
  /Data/DataHarvest
      - twitter data harvester
  /Data/DataAnalysis
      - data analyser 
  /Frontend
      - frontend application
  /data_handle.sh
      - shell for running data harvester and analyser
  /.gitignore
      - avoid uploading meaningless files
```

## **How to Deploy?**
You might need to replace the `/ansible/*openrc.sh` file with your own.

Open your terminal and type in:
```
cd ansible
chmod 600 sshkey.pem
sh run.sh
```
 Then you can have a cup of tea🍵 and wait :-)

## **How to Harvest and Analyze Data in arbitrary instance?**
You just need to run the `data_handle.sh` shell in arbitrary instance belongs to us. Firstly, you are required to access one of our instances using SSH or tools like PUTTY. 

The next step is to run the command below to harvest and analyze *100* tweets: 
```
sh data_handle.sh
```
 If you want to set the amount of data you want to harvest, you may input: 
```
sh data_handle.sh <number of tweets>
```
where an interger would be fine.

You might compare the changes of the database on our [CouchDB administration page](172.26.130.232/5984/_utils) before and after running the shell above.
