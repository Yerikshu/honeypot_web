#!/bin/bash
iptables -D INPUT -j DROP

iptables  -A INPUT -s $1/32 -p tcp -m tcp --dport 550 -j ACCEPT

iptables  -A INPUT -s $1/32 -p tcp -m tcp --dport 80 -j ACCEPT

iptables -A INPUT -j DROP

service iptables save

service iptables restart
