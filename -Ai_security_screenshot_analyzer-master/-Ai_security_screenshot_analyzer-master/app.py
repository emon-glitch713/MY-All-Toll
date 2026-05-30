import streamlit as st
from groq import Groq
from PIL import Image
from fpdf import FPDF
import datetime
import re
import pytesseract

# ---------------- CONFIG ----------------
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="AI Security Screenshot Analyzer",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Security Screenshot Analyzer with OCR")
st.markdown("Upload up to 5 screenshots for OCR-based security report generation.")

# ---------------- PDF FUNCTION ----------------
def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Security Assessment Report", ln=True, align="C")
    pdf.ln(10)

    clean_text = text.encode("latin-1", "ignore").decode("latin-1")
    pdf.multi_cell(0, 10, txt=clean_text)

    return pdf.output(dest="S").encode("latin-1")


# ---------------- SEVERITY PARSER ----------------
def extract_counts(report):
    counts = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for sev in counts.keys():
        matches = re.findall(sev, report, re.IGNORECASE)
        counts[sev] = len(matches)

    return counts


# ---------------- USER INPUT ----------------
target = st.text_input("Target Name", placeholder="example.com")
scope = st.text_input("Scope", placeholder="Login page, admin panel")

uploaded_files = st.file_uploader(
    "Upload screenshots (max 5)",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) > 5:
    st.error("Maximum 5 screenshots allowed.")
    st.stop()

if uploaded_files:
    st.success(f"{len(uploaded_files)} screenshots uploaded")

    all_text = ""

    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file)

        st.image(img, caption=uploaded_file.name, width=250)

        extracted_text = pytesseract.image_to_string(img)
        all_text += extracted_text + "\n\n"

    with st.expander("View Extracted OCR Text"):
        st.text_area("OCR Output", all_text, height=250)

    if st.button("🚀 Generate Report"):
        with st.spinner("Analyzing OCR text and generating report..."):

            try:
                prompt = f"""
Act as a professional cybersecurity consultant.

Analyze the following OCR extracted screenshot text and generate
a structured security assessment report.

Target: {target}
Scope: {scope}

OCR Extracted Text:
{all_text}

IMPORTANT:
Only infer from visible extracted text.
Do not claim live exploitation.

Include these sections:

# Executive Summary
# Scope
# Methodology
# Detailed Findings
# Severity
# Attack Narrative
# Impact
# Recommendations & Remediation

Use severity labels:
Critical, High, Medium, Low
"""

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                report_text = response.choices[0].message.content

                st.success("✅ Report Generated Successfully")

                counts = extract_counts(report_text)

                st.subheader("Severity Overview")

                chart_data = {
                    "Severity": list(counts.keys()),
                    "Count": list(counts.values())
                }

                st.bar_chart(chart_data, x="Severity", y="Count")

                st.markdown("---")
                st.markdown(report_text)

                pdf_data = create_pdf(report_text)

                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_data,
                    file_name=f"security_report_{datetime.date.today()}.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"Error: {e}")

else:
    st.warning("Upload at least 1 screenshot.")


st.divider()
st.caption("© 2026 AI Security Screenshot Analyzer with OCR")
