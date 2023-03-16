#!/usr/bin/python3
import scapy.all as scapy
import argparse
import socket
import time
import napalm


class Discorver:
    ip = ""
    iface = ""
    answered = list()
    unanswered = list()

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--network", dest="network",
                            help="Specify the network you want to reach")
        parser.add_argument("-i", "--iface", dest="iface",
                            help="Specify the output interface")
        options = parser.parse_args()
        self.ip = options.network
        self.iface = options.iface

    def arp(self):
        arp_req = scapy.Arp(pdst=self.ip)
        brd = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_req_brd = brd/arp_req
        self.answered, self.unanswered = scapy.srp(
            arp_req_brd, timeout=1, iface=self.iface)
        for host in self.answered:
            ip, mac = host[1].psrc, host[1].hwsrc
            print(ip, '\t\t' + mac)

    def port(self):
        startTime = time.time()
        for host in self.answered:
            ip = host[1].psrc
            print(ip)
            for i in range(0, 500):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn = s.connect_ex((ip, i))

                if (conn == 0):
                    print('Port %d: OPEN' % (i,))
                    if (i == 22 or i == 23):
                        self.getInfo(ip, i)
                elif (conn == 11):
                    s.close()
                    break
                s.close()
        print("Time taken:", time.time() - startTime)

    def getInfo(self, ip, port):
        driver = napalm.get_network_driver('ios')
        device = driver(hostname=ip, username='user', password='',
                        optional_args={'port': port, 'transport': "ssh"})
        device.open()
        print(device.get_interfaces_ip())
        device.close()


scan = Discorver()
scan.get_args()
scan.arp()
scan.port()
