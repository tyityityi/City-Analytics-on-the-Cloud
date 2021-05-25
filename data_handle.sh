#!/bin/bash

echo "== Set modules =="
sudo apt-get install git
yes|sudo apt install python3-pip
sudo pip3 install couchdb
sudo pip3 install tweepy
sudo pip3 install pandas
sudo pip3 install textblob

echo "== download the codes from github =="
sudo rm -rf City-Analytics-on-the-Cloud/
git clone https://AshleyZ125:xingxia10969@github.com/tyityityi/City-Analytics-on-the-Cloud.git

echo "== run the data harvest and data analysis =="
if [-z"$1"] 
then
sudo python3 ~/City-Analytics-on-the-Cloud/Data/DataHarvest/main.py
else 
sudo python3 ~/City-Analytics-on-the-Cloud/Data/DataHarvest/main.py $1
fi
sudo python3 ~/City-Analytics-on-the-Cloud/Data/DataAnalysis/dedup.py
sudo python3 ~/City-Analytics-on-the-Cloud/Data/DataAnalysis/query.py
sudo python3 ~/City-Analytics-on-the-Cloud/Data/DataAnalysis/analysis.py