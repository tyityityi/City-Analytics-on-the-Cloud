echo "== Set modules =="
sudo apt-get install git
yes|sudo apt install python3-pip
sudo pip3 install couchdb
sudo pip3 install tweepy
sudo pip3 install pandas
sudo pip3 install textblob

echo "== download the codes from github =="
mkdir flask-web
sudo cp docker-compose.yml flask-web/
sudo cp Dockerfile flask-web/
sudo cp requirements.txt flask-web/
cd flask-web
git clone https://AshleyZ125:xingxia10969@github.com/tyityityi/City-Analytics-on-the-Cloud.git

echo "== deploy the frontend codes then run =="
cd ~/flask-web
sudo docker-compose build
sudo docker-compose up -d --remove-orphans


