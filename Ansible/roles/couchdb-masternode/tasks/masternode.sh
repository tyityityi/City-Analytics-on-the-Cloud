#!/bin/bash

echo "== Set modules =="
yes|sudo apt install python3-pip
sudo pip3 install couchdb
sudo pip3 install tweepy
sudo pip3 install pandas
sudo pip3 install textblob
sleep 10

echo "== Set variables =="
declare -a nodes=(172.26.130.232 172.26.128.156 172.26.131.18)
export currnode=172.26.130.232
export user=admin
export password=password

export size=${#nodes[@]}

echo "== Reset the original masternode"
docker stop masternode
docker rm masternode
sleep 3

echo "== Start the container =="
sudo rm -rf /mnt/couchdbdata
mkdir /mnt/couchdbdata
docker run -d -p 5984:5984 -p 5986:5986 -p 4369:4369 -p 9100:9100 -v /mnt/couchdbdata:/opt/couchdb/data --name=masternode couchdb:2.3.0
sleep 3

docker exec masternode bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec masternode bash -c "echo \"-name couchdb@${currnode}\" >> /opt/couchdb/etc/vm.args"

docker restart masternode
sleep 15

echo "== set up database cluster  =="
for (( i=0; i<${size}; i++ )); do
    curl -X PUT "http://${nodes[${i}]}:5984/_node/_local/_config/admins/${user}" --data "\"${password}\""
    sleep 3
    curl -X PUT "http://${user}:${password}@${nodes[${i}]}:5984/_node/couchdb@${nodes[${i}]}/_config/chttpd/bind_address" --data '"0.0.0.0"'
    sleep 2
done

echo "== Add nodes to cluster =="
for (( i=0; i<${size}; i++ )); do
    if [ "${nodes[${i}]}" != "${currnode}" ]; then
        curl -X POST -H 'Content-Type: application/json' http://${user}:${password}@${currnode}:5984/_cluster_setup \
            -d "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \"username\": \"${user}\", \"password\":\"${password}\", \"port\": 5984, \"node_count\": \"${size}\", \
            \"remote_node\": \"${nodes[${i}]}\", \"remote_current_user\": \"${user}\", \"remote_current_password\": \"${password}\"}"
        curl -X POST -H 'Content-Type: application/json' http://${user}:${password}@${currnode}:5984/_cluster_setup \
            -d "{\"action\": \"add_node\", \"host\":\"${nodes[${i}]}\", \"port\": 5984, \"username\": \"${user}\", \"password\":\"${password}\"}"
    fi
done

echo "== Finish cluster =="
curl -X POST -H "Content-Type: application/json" "http://${user}:${password}@${currnode}:5984/_cluster_setup" -d '{"action": "finish_cluster"}'
