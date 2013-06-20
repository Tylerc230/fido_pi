#!/bin/bash
IP=192.168.1.7
rsync --delete -a -v -r --progress ./* $IP:~/pi_fido/
