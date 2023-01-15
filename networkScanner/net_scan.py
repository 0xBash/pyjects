#!/usr/bin python

import scapy.all as scapy
#since optparse is deprecated, new module argparse introduced in this script. 
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broad_arp_rqst = broadcast/arp_request
    #using [0] as there should be 2 parameter but we are using only 1 i.e. answered_list.
    #using verbode=False to output clean formatted output.
    answered_list = scapy.srp(broad_arp_rqst, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return clients_list 
    #Shouldn't we like to enter our ip address CIDR as an argument, i.e. user input for this program.(go to the mac_changer section to learn how to parse user input as an argument.) 
   
def print_results(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_results(scan_result)
