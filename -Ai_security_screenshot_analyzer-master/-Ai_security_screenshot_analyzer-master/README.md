# AI Security Screenshot Analyzer

AI-powered security analysis tool that analyzes screenshots, extracts text using OCR, detects possible vulnerabilities, and generates downloadable PDF security reports.

---

## Features

- Upload up to 5 screenshots
- OCR text extraction with Tesseract
- AI-powered vulnerability analysis
- Security recommendations and findings
- PDF report generation
- Clean Streamlit interface

---

## Demo Screenshot

![Demo](<img width="1366" height="662" alt="WhatsApp Image 2026-05-06 at 05 28 33 (2)" src="https://github.com/user-attachments/assets/81ad72d5-c718-4c4b-b9e4-af67f0a333ab" />
)

> Upload your tool screenshot as `screenshot.png` in this repository.

---

## Installation

```bash
git clone https://github.com/emon-glitch713/-Ai_security_screenshot_analyzer.git
cd -Ai_security_screenshot_analyzer
pip install -r requirements.txt
streamlit run app.py
```

---

## API Key Setup

Create a `.env` file in project folder:

```env
GROQ_API_KEY=your_api_key_here
```

Get API key from:
https://console.groq.com/keys

---

## Usage

1. Run the app
2. Upload screenshots
3. Click Analyze
4. Review AI findings
5. Download PDF security report

---

## Download and Run on Windows

### 1. Download Project
Click **Code** → **Download ZIP**

or clone:

```bash
git clone https://github.com/emon-glitch713/-Ai_security_screenshot_analyzer.git
```

### 2. Extract ZIP
Extract the ZIP file.

### 3. Install Python
Download Python from:
https://www.python.org/downloads/

During installation enable:

- Add Python to PATH

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Setup API Key

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Run Application

```bash
streamlit run app.py
```

### 7. Open Browser

Visit:

```bash
http://localhost:8501
```

---

## Tech Stack

- Python
- Streamlit
- Groq API
- Tesseract OCR
- FPDF

---

## Project Structure

```bash
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshot.png
```

---

## Author

Created by **emon-glitch713**

GitHub:
https://github.com/emon-glitch713
