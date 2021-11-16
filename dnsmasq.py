import subprocess as sp

with open('interface.txt','r') as fd:
    interface=fd.read()

masq_info='''interface={}
dhcp-range=192.168.1.2, 192.168.1.30, 255.255.255.0, 12h
dhcp-option=3, 192.168.1.1
dhcp-option=6, 192.168.1.1
server=8.8.8.8
log-queries
log-dhcp
listen-address=127.0.0.1
address=/#/192.168.1.1'''.format(interface)
#address=/#/192.168.1.1
#server=8.8.8.8
#cd dns;python masq.py dhcp-alternate-port = 5000
with open('dnsmasq.conf','w') as fd:
    fd.write(masq_info)

'''
sp.run('iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE'.split(' '))
sp.run('iptables --append FORWARD --in-interface {} -j ACCEPT'.format(interface).split(' '))
sp.run('echo 1 > /proc/sys/net/ipv4/ip_forward'.split(' '))
'''

sp.run(['ifconfig',interface,'up','192.168.1.1', 'netmask', '255.255.255.0'])
sp.run('route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1'.split(' '))
sp.run('dnsmasq -C dnsmasq.conf -d'.split(' '))
