import socket
import fcntl
import struct
import netifaces as ni

def get_ip_address(ifname):
    return ni.ifaddresses(ifname)[2][0]["addr"]

def get_ip_list(ifname):
    ipstring = ""
    try:
        ipstring = get_ip_address(ifname)
    except:
        pass

    ipList = None
    if len(ipstring) > 0:
        ipList = ipstring.split('.')

    return ipList

if __name__ == '__main__':
    print(get_ip_address('eth0'))

