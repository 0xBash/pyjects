#!/usr/bin/ python

import subprocess
import optparse
import re


#def available_interfaces():
    


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")
    (options, arguments) = parser.parse_args()
    #conditional statements
    if not options.interface:
        #code to handle_error
        print("[-] Please enter the interface name, use --help for more info.")
    elif not options.new_mac:
        #code to handle errors
        print("[-] Please enter the new MAC Address, use --help for more info.")
    return options
    
def macchange(interface, new_mac):
    print("[+] The interface > " + interface + " will change its mac address to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifcon_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_reslt = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifcon_result))

    if mac_addr_reslt:
       return mac_addr_reslt.group(0)
    else:
        print("[-] Could not get the MAC address.")

options = get_args()

curr_mac = get_current_mac(options.interface)
print("Current MAC = " + str(curr_mac))

macchange(options.interface, options.new_mac)

#After above function's execution "curr_mac" value will get changed.
final_mac = get_current_mac(options.interface)

if curr_mac == options.new_mac:
    print("[-] MAC Address not changed.")
elif final_mac == options.new_mac:
    print("[+] MAC Address has been chaged to " + final_mac)