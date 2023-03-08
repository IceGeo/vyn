#!/usr/bin/python3
import scapy.all as scapy
import argparse


class Discorver:
    ip = ""
    iface = ""
   
    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--network", dest="network", help="Specify the network you want to reach")
        parser.add_argument("-i", "--iface", dest="iface", help="Specify the output interface")
        options = parser.parse_args()
        self.ip = options.network
        self.iface = options.iface
   
    def arp(self, ip, iface):
        arp_req = scapy.ARP(pdst=self.ip)
        brd = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_req_brd = brd/arp_req
        answered, unanswered = scapy.srp(arp_req_brd, timeout=1, iface=self.iface)
        for host in answered:
            ip, mac = host[1].psrc, host[1].hwsrc
            print(ip, '\t\t' + mac)


scan = Discorver()
scan.get_args()
scan.arp()