<h1>Intended for Debian Linux</h1>

<h2>Description:</h2>

This program helps in achieving man in the middle by sending a poisoned arp packet to the gateway and the desired target. which will then force the target traffic to flow through the Hakers OS.

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

