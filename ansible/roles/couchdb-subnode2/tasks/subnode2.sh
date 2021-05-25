#!/bin/bash

echo "== Set modules =="
yes|sudo apt install python3-pip
sudo pip3 install couchdb
sudo pip3 install tweepy
sudo pip3 install pandas
sudo pip3 install textblob
sleep 5

echo "== Set variables =="
export node=172.26.131.18
export user=admin
export password=password

echo "== Reset the original subnode2"
docker stop subnode2
docker rm subnode2
sleep 3

echo "== Start the containers =="
sudo rm -rf /mnt/couchdbdata
mkdir /mnt/couchdbdata
docker run -d -p 5984:5984 -p 5986:5986 -p 4369:4369 -p 9100:9100 -v /mnt/couchdbdata:/opt/couchdb/data --name=subnode2 couchdb:2.3.0
sleep 3

docker exec subnode2 bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec subnode2 bash -c "echo \"-name couchdb@${node}\" >> /opt/couchdb/etc/vm.args"

docker restart subnode2
sleep 3
