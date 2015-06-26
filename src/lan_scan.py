#!/usr/bin/python

# LAN Scanner
# 

# ---------- [Description]
# A very simple LAN scanner which shows MAC and IP addresses.

# ---------- [Features]
# - Shows you the MAC and IP of a running system.
# - Creates a small log file.

# ---------- [Usage example]
# python lan_scan.py --network=192.168.1.0/24 

# ---------- [Tested with]
# - Python 2.7.3

# ---------- [Notes]
# - Modify, distribute, share and copy this code in any way you like!
# - Please note that this tool was created and published for educational purposes only.

#/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Author: by Valentin Hoebel (valentin@xenuser.org)
# Developer: Goncalo Bejinha

import sys,  getopt
from scapy.all import srp,Ether,ARP,conf
from time import gmtime, strftime

def print_usage():
    print_banner()
    print "[!] Wrong argument and parameter passed. Use --help for more information."
    print "[!] Usage: sudo ./lan_scan.py --network=<your network>"
    print "[i] Usage Example: sudo ./lan_scan.py --network=192.168.1.0/24"
    print ""
    print ""
    sys.exit()
    return
    
def print_help():
    print_banner()
    print ""
    print "[Description]"
    print "The LAN Scanner tries to show you"
    print "the MAC and IP addresses of all running systems"
    print "in your local network."
    print ""
    print "[Usage]"
    print "python lan_scan.py --network=<your network>"
    print ""
    print "[Usage example]"
    print "python lan_scan.py --network=192.168.1.0/24"
    print ""
    print "[Feature list]"
    print "- Shows you the MAC and IP of a running system."
    print "- Creates a small log file."
    print ""
    print "[Installation]"
    print "- Requires package python-scapy."
    print ""
    print "[Some notes]"
    print "- Tested with Python 2.7.3."
    print "- Modify, distribute, share and copy the code in any way you like!"
    print "- Please note that this tool was created for educational purposes only."
    print "- Do not use this tool in an illegal way. Know and respect your local laws."
    print ""
    print ""
    sys.exit()    
    return
    
def print_banner():
    print ""
    print ""
    print "LAN Scanner"
    print ""
    print "Version 1.0 (LPD 2015)"
    print "____________________________________________________"
    print ""
    return
    
def scan_lan(scan_network):
    conf.verb=0
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=scan_network),timeout=2)
    print ""
    
    log_file=strftime("%d_%b_%Y_%H:%M:%S_+0000", gmtime()) + "_-_scan.log"
    FILE = open(log_file,  "w")
    FILE.write("LAN Scanner - Log File\n")
    FILE.write("----------------------------------------\n")
    FILE.write("[+] Scanned network: " + scan_network + "\n")
    FILE.write("[+] Scan time: " + strftime("%d %b %Y, %H:%M:%S +0000 GMT", gmtime()) + "\n")
    FILE.write("\n")
    
    for snd,rcv in ans:
        mac_address=rcv.sprintf("%Ether.src%")
        ip_address=rcv.sprintf("%ARP.psrc%")
        
        print rcv.sprintf("[+] Found a system! MAC: %Ether.src% IP: %ARP.psrc% ")
        FILE.write(ip_address + ", " + mac_address + "\n")
    
    FILE.write("\n")
    FILE.close
    print ""
    print "[i] Completed the scan. Exiting now!"
    print ""
    print ""
    return
    

def main(argv):
    scan_network=""
    
    try:
        opts,  args = getopt.getopt(sys.argv[1:],  "",  ["help",  "network="])
    except getopt.GetoptError   :
        print_usage()
        sys.exit(2)
    
    for opt,  arg in opts:
        if opt in ("--help"):
            print_help()
            break
            sys.exit(1)
        elif opt in ("--network") :
            scan_network=arg
            
    if len(scan_network) < 1:
        print_usage()
        sys.exit()
        
    print_banner()
    print "[i] Provided network to scan: " + scan_network
    scan_lan(scan_network)

if __name__ == "__main__":
    main(sys.argv[1:])
### EOF ###
