#!/usr/bin/env python3
# Fonts: https://yaytext.com/monospace/
# Emoji: https://emojipedia.org/en/search?q=address

# 🔧 MAC Address Changer Utility
# 🛡️ Author: Master Anon (https://github.com/Anonymoussxb)
# 📅 Date: 2025-05-17
# 📝 Description: This tool allows you to spoof/change your MAC address 
#     on a specified network interface for anonymity or security testing.
# ⚠️ Note: Requires sudo/root privileges to modify network interfaces.


import subprocess, argparse, re

def add_arguments():
    '''📥 𝗣𝗮𝗿𝘀𝗲 𝗖𝗟𝗜 𝗮𝗿𝗴𝘂𝗺𝗲𝗻𝘁𝘀: 𝗧𝗮𝗸𝗲𝘀 𝗶𝗻𝘁𝗲𝗿𝗳𝗮𝗰𝗲 𝗮𝗻𝗱 𝗻𝗲𝘄 𝗠𝗔𝗖 𝗮𝗱𝗱𝗿𝗲𝘀𝘀'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="📌 𝙸𝚗𝚝𝚎𝚛𝚏𝚊𝚌𝚎 𝚝𝚘 𝚌𝚑𝚊𝚗𝚐𝚎 𝙼𝚊𝚌 𝙰𝚍𝚍𝚛𝚎𝚜𝚜 📌")
    parser.add_argument("-m", "--mac", dest="new_mac", help="🔥 𝙽𝚎𝚠 𝙼𝚊𝚌 𝙰𝚍𝚍𝚛𝚎𝚜𝚜 🔥")
    return parser.parse_args()


def mac_adr_change():
    '''🔄 𝗖𝗵𝗮𝗻𝗴𝗲 𝘁𝗵𝗲 𝗠𝗔𝗖 𝗮𝗱𝗱𝗿𝗲𝘀𝘀 𝗼𝗳 𝗮 𝗻𝗲𝘁𝘄𝗼𝗿𝗸 𝗶𝗻𝘁𝗲𝗿𝗳𝗮𝗰𝗲 (𝗹𝗶𝗻𝘂𝘅-𝗼𝗻𝗹𝘆)
    🧪 Reads the current MAC, shuts down the interface, applies the new MAC, and verifies the change
    🚨 Must be run with sudo/root privileges
    '''
    info = add_arguments()

    if not info.interface:
        print("❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚙𝚎𝚌𝚒𝚏𝚢 𝚊𝚗 𝚒𝚗𝚝𝚎𝚛𝚏𝚊𝚌𝚎 — 𝚞𝚜𝚎 --𝚑𝚎𝚕𝚙 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚒𝚗𝚏𝚘")
        return
    if not info.new_mac:
        print("❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚙𝚎𝚌𝚒𝚏𝚢 𝚊 𝚗𝚎𝚠 𝙼𝙰𝙲 𝙰𝚍𝚍𝚛𝚎𝚜𝚜 — 𝚞𝚜𝚎 --𝚑𝚎𝚕𝚙 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚒𝚗𝚏𝚘")
        return
    
    result = subprocess.check_output(["ifconfig", info.interface]).decode()
    intial_mac = re.search(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", result)
    if intial_mac:
        intial_mac = intial_mac.group(0)

        print(f"🔧 𝙲𝚑𝚊𝚗𝚐𝚒𝚗𝚐 𝙼𝙰𝙲 𝙰𝚍𝚍𝚛𝚎𝚜𝚜 𝚏𝚘𝚛 ➤ `{info.interface}`\n")
        print(f"🧬 𝙵𝚛𝚘𝚖 ➤ {intial_mac}")
        print(f"🚀 𝚃𝚘 ➤ {info.new_mac}\n")

        subprocess.call(f"ifconfig {info.interface} down", shell=True)
        subprocess.call(f"ifconfig {info.interface} hw ether {info.new_mac}", shell=True)
        result = subprocess.check_output(["ifconfig", info.interface]).decode()
        final_mac = re.search(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", result).group(0)

        print(f"✅ 𝙈𝘼𝘾 𝘈𝘥𝘥𝘳𝘦𝘴𝘴 𝘊𝘩𝘢𝘯𝘨𝘦𝘥 𝘚𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺!\n")
        print(f"🧾 {intial_mac} ➡️  {final_mac}")
    else:
        print("❌ 𝘾𝙤𝙪𝙡𝙙 𝙣𝙤𝙩 𝙧𝙚𝙖𝙙 𝙘𝙪𝙧𝙧𝙚𝙣𝙩 𝙈𝘼𝘾 𝙖𝙙𝙙𝙧𝙚𝙨𝙨!")
        print("📛 𝙈𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙞𝙣𝙩𝙚𝙧𝙛𝙖𝙘𝙚 𝙚𝙭𝙞𝙨𝙩𝙨 𝙖𝙣𝙙 𝙝𝙖𝙨 𝙖 𝙈𝘼𝘾 𝙖𝙙𝙙𝙧𝙚𝙨𝙨 ❗")

mac_adr_change()
