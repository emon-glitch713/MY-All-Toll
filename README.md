# 🛠️ All-in-One Cyber Security Frameworks & Toolkits

Welcome to the master repository of my custom-built cyber security, OSINT, AI-powered analysis, network auditing, and directory scanning tools. These utilities are developed using Python and Bash Script, optimized for Kali Linux, Termux, and Windows environments.

<p align="center">
  <img src="screenshot.png" alt="Framework Master Screenshot" width="750">
</p>

---

## 🚀 Tools Showcase & Overview

### 🐉 1. J-Emon Ultimate Security Framework v8.0
A powerful all-in-one Network & Web Reconnaissance tool built for Kali Linux.
- **Key Features:** Advanced network recon, IP/MAC & brand vendor identification of all live hosts on Wi-Fi, real-time tracking with an audible sound alarm system, and precise IP geolocation metadata extraction.
- **Directory:** `/j_emon_framework`
- **Execution Command:** `sudo python3 my_scanner.py -t 192.168.1.1/24`

### 🧰 2. Cyber Toolkit (Cross-Platform)
A comprehensive terminal-based security Swiss Army knife compatible with Linux and Android (Termux).
- **Key Features:** Deep vulnerability scanning via automated scripts, web infrastructure auditing (SQL Injection indicator & XSS reflection checks), SSL verification, hashing utilities, and a secure password generator.
- **Directory:** `/Cyber_Toolkit`
- **Execution Command:** `python3 my_scanner.py -t <Target>`

### 📸 3. Flask Advanced Device Tracker & IP Logger
An advanced web-based OSINT tracking simulation framework that gathers deep device parameters stealthily through a video-streaming cover interface.
- **Key Features:** Server-side backend IP & ISP tracking, real-time JavaScript device profiling (battery health, charging status, hardware screen resolutions, network downlink speed), and accurate user-agent device model/brand detection.
- **Directory:** `/flask_tracker`
- **Execution Command:** `python3 app.py`

### 🤖 4. AI Security Screenshot Analyzer
A cutting-edge AI-driven application designed to analyze system screenshots, extract terminal logs via OCR, evaluate risks using modern LLMs, and compile comprehensive, downloadable executive reports.
- **Key Features:** Tesseract OCR engine text extraction, state-of-the-art vulnerability contextual analysis using Groq API (LLM), structured report compiling via FPDF layout architecture, and an elegant Streamlit web user interface.
- **Directory:** `/Ai_security_screenshot_analyzer`
- **Execution Command:** `streamlit run app.py`

### 🔍 5. Dirsearch Auto Scanner
A modular Shell execution script designed to completely automate web endpoint path enumeration and hidden directory discovery routines.
- **Key Features:** Single-command execution parameters. Features built-in automatic dependency evaluation—if the core `dirsearch` utility is missing from the system path, the script safely clones, provisions, and provisions the engine autonomously.
- **Directory:** `/dirsearch-auto-scan`
- **Execution Command:** `chmod +x scan.sh && ./scan.sh`

---

## 💻 Installation & Environment Provisioning

### 🐧 Linux (Kali Linux / Ubuntu Deployment):
```bash
# Clone the unified ecosystem repository
git clone https://github.com
cd my-security-framework

# Provision baseline binaries and system requirements
sudo apt update && sudo apt install nmap sox tesseract-ocr dirsearch -y
pip install -r requirements.txt --break-system-packages
```

### 📱 Termux (Android Native Deployment):
```bash
pkg update && pkg upgrade -y
pkg install python git nmap -y
git clone https://github.com
cd my-security-framework
pip install -r requirements.txt
```

### 🪟 Windows Setup (Optimized for AI Screenshot Analyzer):
1. Navigate directly into the project directory root.
2. Initialize environment requirements: `pip install -r requirements.txt`
3. Setup an environment variables configuration file (`.env`) inside the path: `GROQ_API_KEY=your_api_key_here`
4. Deploy the execution instance via terminal: `streamlit run Ai_security_screenshot_analyzer/app.py`

---

## 👤 Developer Profiles & Background
**Jubed-Emon**
- Cyber Security Enthusiast, Penetration Tester & Python Systems Developer
- 🔗 **GitHub Profile:** [emon-glitch713](https://github.com)

---

## ⚠️ Academic Disclaimer
This suite is strictly intended for educational exercises, academic research, and authorized white-hat infrastructure defense auditing. The author explicitly disclaims any liability for malicious execution or structural compromises caused by improper or unauthorized utility deployment.
