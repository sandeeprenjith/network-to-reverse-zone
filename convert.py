#!/usr/bin/python3

import sys 
import re
net = sys.argv[1]
net_pattern = re.compile('^([0-9]{1,3}\.){3}[0-9]{1,3}($|/(8|16|24))$')
if not re.match(net_pattern, net):
    sys.exit('Invalid network. Expected <net>/<cidr>. Example: 192.168.0.0/24. Only /8, /16 and /24 are supported')

net_cidr = net.split('/')
net_addr = net_cidr[0]
cidr = net_cidr[1]

octets = net_addr.split('.')
if int(cidr) == 24:
    octets.pop(3)
elif int(cidr) == 16:
    octets.pop(3)
    octets.pop(2)
elif int(cidr) == 8:
    octets.pop(3)
    octets.pop(2)
    octets.pop(1)

octets.reverse()
print('.'.join(octets) + '.in-addr.arpa')
