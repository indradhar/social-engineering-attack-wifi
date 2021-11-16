import subprocess as sp

iw=sp.run(['iwconfig'],capture_output=True, text= True).stdout
interface=iw.split(' ')[0]
if 'monitor' not in iw.lower():
    check_kill=sp.run(['airmon-ng','check','kill'],capture_output=True, text= True).stdout
    stop=sp.run(['airmon-ng','stop',interface],capture_output=True, text= True).stdout
    print(check_kill,stop)
    start=sp.run(['airmon-ng','start',interface],capture_output=True, text= True).stdout
    print(start)
else:
    print('yes')

iw=sp.run(['iwconfig'],capture_output=True, text= True).stdout
interface=iw.split(' ')[0]

with open('hostapd.conf','w') as fd:
    ap_info='''interface={}
driver=nl80211
ssid=Engineering-Library
hw_mode=g
channel= 1
macaddr_acl=0
ignore_broadcast_ssid=0'''.format(interface)
    fd.write(ap_info)
with open('interface.txt','w') as fd:
    fd.write(interface)
sp.run(['hostapd', 'hostapd.conf'])
