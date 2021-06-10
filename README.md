# network-to-reverse-zone
Script to print reverse mapping zone name from network

Usage Examples:

```
./convert.py 10.0.0.0/8
10.in-addr.arpa
./convert.py 10.0.0.0/16
0.10.in-addr.arpa
./convert.py 10.0.0.0/24
0.0.10.in-addr.arpa
./convert.py 10.0.0.0/12
Invalid network. Expected <net>/<cidr>. Example: 192.168.0.0/24. Only /8, /16 and /24 are supported
```


