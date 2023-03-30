from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP, srp
# import argparse
import socket
import time
import napalm


class scan:
    ip = ""
    iface = ""
    answered = list()
    unanswered = list()
    # ################# Ancienne méthode ##################
    # def get_args(self):
    #    parser = argparse.ArgumentParser()
    #    parser.add_argument("-n", "--network", dest="network",
    #                        help="Specify the network you want to reach")
    #    parser.add_argument("-i", "--iface", dest="iface",
    #                        help="Specify the output interface")
    #    options = parser.parse_args()
    #    self.ip = options.network
    #    self.iface = options.iface
  
    def __init__(self, ip, iface):
        self.ip = ip
        self.iface = iface

    def arp(self):
        arp_req = ARP(pdst=self.ip)
        brd = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_req_brd = brd/arp_req
        self.answered, self.unanswered = srp(
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
