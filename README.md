<h1>Intended for Debian Linux</h1>

<h2>Description:</h2>

This script facilitates a man-in-the-middle attack by transmitting a malicious ARP packet to both the gateway and the intended target, compelling the target's traffic to pass through the attacker's operating system.
<h2>Prerequsite</h2>

pip install sys

pip install time

pip install scapy.all

pip install optparse

pip install re

pip install subprocess

<h2>Usage: </h2>

python arp_spoofer.py -t (target IP) -g (target gateway IP)

or

python arp_spoofer.py --help

