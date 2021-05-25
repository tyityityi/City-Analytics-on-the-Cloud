#!/bin/bash

# launch instances and implement templates
#. ./unimelb-comp90024-2021-grp-66-openrc.sh;ansible-playbook --ask-become-pass mrc.yml

# install docker on the remote servers
#ansible-playbook -i inventory.ini -u ubuntu --key-file=./sshkey docker.yml

# set up couchdb as cluster
#ansible-playbook -i inventory.ini -u ubuntu --key-file=./sshkey couchdb_cluster.yml

# deploy data harvest works and web server
ansible-playbook -i inventory.ini -u ubuntu --key-file=./sshkey application.yml
