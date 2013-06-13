#!/bin/bash
IP=192.168.1.7
rsync -a --progress ./* $IP:~/pi_fido/
