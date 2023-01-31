#!/usr/bin/ python
import netfilterqueue

    #IPTABLES command for making our packet storing queue :D
    #
    #iptables -I FORWARD -j NFQUEUE --queue-num 0
    #iptables -I OUTPUT -j NFQUEUE --queue-num 0
    #iptables -I INPUT -j NFQUEUE --queue-num 0
    #

#callback_function
def process_packet(packet):
    print(packet)
    #packet.drop()
    #packet.accept()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()