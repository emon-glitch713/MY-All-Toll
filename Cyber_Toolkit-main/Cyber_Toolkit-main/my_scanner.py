kkimport scapy.all as scapy
from mac_vendor_lookup import MacLookup
import nmap
import argparse
import time
import sys
import requests
from termcolor import colored
from tqdm import tqdm

def print_banner():
    banner = f"""
    {colored('='*70, 'magenta')}
    {colored('║', 'magenta')} {colored('      JUBED-EMON ULTIMATE NETWORK & SECURITY AUDITOR       ', 'cyan', attrs=['bold'])} {colored('║', 'magenta')}
    {colored('║', 'magenta')} {colored('        Vulnerability Scan | Monitoring | Geolocation      ', 'white')} {colored('║', 'magenta')}
    {colored('='*70, 'magenta')}
    """
    print(banner)

# ফিচার ৩: আইপি জিওলোকেশন (বাইরের আইপির জন্য)
def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com{ip}").json()
        if response['status'] == 'success':
            return f"{response['city']}, {response['country']}"
    except:
        return "Local/Unknown"
    return "Local"

# ফিচার ১: পাওয়ারফুল স্ক্যান ও দুর্বলতা খোঁজা
def scan(target):
    nm = nmap.PortScanner()
    vendor_lookup = MacLookup()
    print(colored(f"\n[*] Starting Deep Recon & Vuln Scan on: {target}", "blue", attrs=['bold']))
    
    for i in tqdm(range(100), desc="Analyzing", ncols=75):
        time.sleep(0.02)
    
    # Nmap Vuln Scan (খুবই পাওয়ারফুল কমান্ড)
    nm.scan(hosts=target, arguments='-sV --script vuln -F') 

    print(colored("\nIP Address\tLocation\tVendor/OS\t\tVulns & Services", "green", attrs=['bold']))
    print(colored("-" * 100, "blue"))

    for host in nm.all_hosts():
        loc = get_location(host)
        
        try:
            mac = nm[host]['addresses'].get('mac', 'Unknown')
            vendor = vendor_lookup.lookup(mac) if mac != 'Unknown' else "Device"
        except: vendor = "Unknown"

        # সার্ভিস ও দুর্বলতা চেক
        vulns = []
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                service = nm[host][proto][port]['name']
                # এখানে দুর্বলতা থাকলে সেটি আসবে
                if 'script' in nm[host][proto][port]:
                    vulns.append(f"{port}(VULNERABLE!)")
                else:
                    vulns.append(f"{port}({service})")
        
        vuln_str = ", ".join(vulns) if vulns else "Secure"
        print(f"{colored(host, 'white')}\t{colored(loc[:15], 'yellow')}\t{colored(vendor[:15], 'cyan')}\t{colored(vuln_str, 'red')}")

# ফিচার ২: লাইভ মনিটরিং মোড
def monitor_network(target):
    print(colored(f"\n[!] Monitoring Mode Active on {target}... Press Ctrl+C to stop.", "yellow", attrs=['bold']))
    known_devices = []
    
    while True:
        arp_request = scapy.ARP(pdst=target)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        answered_list = scapy.srp(broadcast/arp_request, timeout=1, verbose=False)[0]
        
        for element in answered_list:
            ip = element[1].psrc
            if ip not in known_devices:
                print(colored(f"\n[NEW DEVICE] {ip} just connected to your network!", "red", attrs=['blink', 'bold']))
                known_devices.append(ip)
        time.sleep(5)

if __name__ == "__main__":
    print_banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/Range")
    parser.add_argument("-m", "--monitor", action="store_true", help="Enable Live Monitoring")
    args = parser.parse_args()

    if not args.target:
        print(colored("[-] Usage: sudo python3 my_scanner.py -t <IP Range>", "red"))
    elif args.monitor:
        monitor_network(args.target)
    else:
        try:
            scan(args.target)
        except KeyboardInterrupt:
            print("\nStopped.")
