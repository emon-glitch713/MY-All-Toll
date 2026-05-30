# 🐉 J-Emon Ultimate Security Framework v8.0
A powerful, all-in-one Network & Web Reconnaissance tool built with Python for Kali Linux. Developed by **Jubed-Emon**.

## 🔥 Key Features
- **Advanced Network Recon:** Detects all devices in your WiFi with IP, MAC, and Brand (Vendor) identification.
- **Port & Service Scanning:** Scans for open ports and identifies running services.
- **Security Suggestions:** Provides expert-level tips for every vulnerability found.
- **Live Monitoring:** Real-time device connection alerts with an audible sound alarm.
- **Web URL Analysis:** Resolves domains to IPs and scans web servers for security auditing.
- **IP Geolocation:** Finds the country, city, and Google Maps location of any public IP.

## 🛠️ Installation & How to Use

### 1. Prerequisites
Before running the tool, ensure you have the following installed on your Kali Linux:
```bash
sudo apt update
sudo apt install nmap sox -y
sudo pip install scapy python-nmap mac-vendor-lookup termcolor tqdm requests --break-system-packages
```

### 2. Download/Clone the Tool
To download this tool to your machine, run:
```bash
git clone https://github.com
cd my-Security-Framework
```

### 3. Running the Tool
Use the following commands to explore different features:

- **Full Network Scan:**
  ```bash
  sudo python3 my_scanner.py -t 192.168.2.1/24
  ```
- **Live Monitoring Mode (Alarm Active):**
  ```bash
  sudo python3 my_scanner.py -t 192.168.2.1/24 -m
  ```
- **Web URL Scan:**
  ```bash
  sudo python3 my_scanner.py -t google.com
  ```
- **Traffic Sniffing:**
  ```bash
  sudo python3 my_scanner.py -s eth0
  ```
- **IP Geolocation:**
  ```bash
  sudo python3 my_scanner.py -l 8.8.8.8
  ```

## 👤 Developer
**Jubed-Emon**
- Cyber Security Enthusiast & Python Developer
- [GitHub Profile](https://github.com/emon-glitch713)

---
