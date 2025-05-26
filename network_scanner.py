#!/usr/bin/env python3
# 🌐 Network Device Scanner
# 🛡️ Author: Master Anon (https://github.com/Anonymoussxb)
# 📅 Date: 2025-05-22
# 📝 Description: This script scans for devices on a given subnet/IP range 
#     and displays active IP and MAC addresses in a table.
# 📦 Dependencies: scapy, prettytable
# ⚠️ Note: Works best on Linux with sudo privileges. Designed for internal network enumeration.



import argparse, scapy.all as scapy
from prettytable import PrettyTable 


def get_arguments():
    '''📥 𝗧𝗮𝗸𝗲 𝘁𝗮𝗿𝗴𝗲𝘁 𝗜𝗣 𝗿𝗮𝗻𝗴𝗲 𝗳𝗿𝗼𝗺 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗶𝗻𝗲
    Example: -t 192.168.1.1/24
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="ip", help="📡 𝚂𝚙𝚎𝚌𝚒𝚏𝚢 𝙸𝙿 𝚝𝚘 𝚋𝚎 𝚂𝚌𝚊𝚗𝚗𝚎𝚍!")
    return parser.parse_args()
    

def print_result(result):
    '''📊 𝗙𝗼𝗿𝗺𝗮𝘁 𝗮𝗻𝗱 𝗽𝗿𝗶𝗻𝘁 𝘀𝗰𝗮𝗻 𝗿𝗲𝘀𝘂𝗹𝘁𝘀 𝗶𝗻 𝗮 𝘁𝗮𝗯𝗹𝗲
    Displays IP and MAC address of active devices on the network
    '''
    print("\n📋 𝙳𝚎𝚟𝚒𝚌𝚎 𝚂𝚌𝚊𝚗 𝚁𝚎𝚜𝚞𝚕𝚝𝚜 🔍\n")
    
    table = PrettyTable()
    table.field_names = ["🌐 𝙸𝙿 𝙰𝚍𝚍𝚛𝚎𝚜𝚜", "🔐 𝙼𝙰𝙲 𝙰𝚍𝚍𝚛𝚎𝚜𝚜"]

    for element in result:
       table.add_row([f"🖥️  {element[1].psrc}", f"🧬  {element[1].hwsrc}"])
    
    print(table)
    print("\n✅ 𝚂𝚌𝚊𝚗 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚍 ✅")


def scan():
    '''🔍 𝗦𝗲𝗻𝗱 𝗔𝗥𝗣 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝘁𝗼 𝗹𝗼𝗰𝗮𝗹 𝗻𝗲𝘁𝘄𝗼𝗿𝗸
    Uses Scapy to build ARP requests and broadcasts them to the given IP range.
    Receives replies and passes the results for display.
    '''
    info = get_arguments()
    arp_request = scapy.ARP(pdst=info.ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast =  broadcast/arp_request
    result = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print_result(result)
    
        
scan()
