import scapy.all as scapy
from mac_vendor_lookup import MacLookup
import nmap
import argparse
import time
import socket
import os
import requests
from termcolor import colored
from tqdm import tqdm

# --- ড্রাগন লোগো স্টাইল ব্যানার ---
def print_banner():
    banner = f"""
{colored('                   ,           ,', 'red')}
{colored('                  /             \\', 'red')}
{colored('                 ((__-^^-,-^^-__))', 'red')}
{colored('                  `-_---" "---_-\'', 'red')}
{colored('                   `--|o` \'o|--\'', 'red')}
{colored('                      \\  `  /', 'red')}
{colored('                       < - >', 'red')}
{colored('                        < >', 'red')}
{colored('                        | |', 'red')}
{colored('       _________________| |_________________', 'magenta')}
{colored('      |                                     |', 'magenta')}
{colored('      |    JUBED-EMON ULTIMATE FRAMEWORK    |', 'cyan', attrs=['bold'])}
{colored('      |        STATUS: DRAGON ACTIVE        |', 'yellow')}
{colored('      |_____________________________________|', 'magenta')}
    """
    print(banner)

def play_alarm():
    os.system("play -nq -t alsa synth 0.5 sine 440 > /dev/null 2>&1")

def get_suggestion(service):
    suggestions = {"ftp": "Disable Anon Login", "http": "Use SSL/HTTPS", "ssh": "Use Key-Auth", "telnet": "Insecure! Use SSH"}
    return suggestions.get(service.lower(), "Service Active")

# ফিচার ১: স্ক্যানার (ডিভাইস কাউন্টসহ)
def scan(target):
    nm = nmap.PortScanner()
    vendor_lookup = MacLookup()
    print(colored(f"[*] Recon started by Jubed-Emon on: {target}", "blue", attrs=['bold']))
    
    for i in tqdm(range(100), desc="Analyzing", ncols=75): time.sleep(0.01)
    
    nm.scan(hosts=target, arguments='-sV -F')
    
    print(colored("\nIP Address\tDevice Vendor\t\tOpen Ports & Suggestions", "green", attrs=['bold']))
    print(colored("-" * 105, "blue"))

    device_count = 0
    for host in nm.all_hosts():
        device_count += 1
        try:
            mac = nm[host]['addresses'].get('mac', 'Unknown')
            vendor = vendor_lookup.lookup(mac) if mac != 'Unknown' else "Local Device"
        except: vendor = "Unknown"
        
        services = []
        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                srv_name = nm[host]['tcp'][port]['name']
                sug = get_suggestion(srv_name)
                services.append(f"{port}({srv_name}: {sug})")
        
        service_str = ", ".join(services) if services else "Secure/No Ports"
        print(f"{colored(host, 'white')}\t{colored(vendor[:18], 'cyan')}\t\t{service_str}")

    print(colored("-" * 105, "blue"))
    print(colored(f"\n[+] Total Active Devices in your Wifi: {device_count}", "yellow", attrs=['bold']))

# ফিচার ২: লাইভ মনিটর
def monitor(target):
    print(colored(f"[*] Monitoring {target}... Alarm is ON!", "magenta", attrs=['bold']))
    known = []
    while True:
        try:
            ans, _ = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=target), timeout=2, verbose=False)
            for _, rcv in ans:
                if rcv.psrc not in known:
                    print(colored(f"\n[!] ALERT: New Device {rcv.psrc} connected!", "red", attrs=['bold', 'blink']))
                    play_alarm()
                    known.append(rcv.psrc)
            time.sleep(5)
        except KeyboardInterrupt: break

if __name__ == "__main__":
    print_banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="IP Range (e.g. 192.168.2.1/24)")
    parser.add_argument("-m", "--monitor", action="store_true", help="Enable Monitor")
    args = parser.parse_args()

    if args.monitor:
        monitor(args.target)
    elif args.target:
        scan(args.target)
