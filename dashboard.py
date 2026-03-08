
import streamlit as st
import requests
import smtplib
from email.mime.text import MIMEText
from streamlit_autorefresh import st_autorefresh

# -------- CONFIG --------
CHANNEL_ID = "3246206"
READ_API_KEY = "TXIWORZUI39VRRFQ"
URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"

# -------- EMAIL CONFIG --------
sender_email = "vehiclemoniteralert@gmail.com"
receiver_email = "yuv9079@gmail.com"
app_password = "asol rrhh lxik ccnw"

st_autorefresh(interval=15000, key="refresh")

st.set_page_config(
    page_title="Vehicle Health Monitoring System",
    layout="centered"
)

# -------- EMAIL FUNCTION --------
def send_email_alert(subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
    except:
        pass

# -------- CSS --------
st.markdown("""
<style>
.header {
    background-color: #1f2933;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 25px;
}
.header h1 { color: white; font-size: 34px; }
.header p { color: #cbd5e1; }
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
.label { font-size: 14px; color: #6c757d; }
.value { font-size: 24px; font-weight: bold; color: #212529; }
.status-box {
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    color: white;
    font-size: 22px;
    font-weight: bold;
    margin-top: 15px;
}
.reason { font-size: 16px; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown("""
<div class="header">
    <h1>🚗 Vehicle Health Monitoring System</h1>
    <p>Live Data from ThingSpeak Cloud</p>
</div>
""", unsafe_allow_html=True)

if "last_status" not in st.session_state:
    st.session_state.last_status = "HEALTHY"

try:
    r = requests.get(URL, timeout=10)
    data = r.json()

    if "feeds" in data and len(data["feeds"]) > 0:
        feed = data["feeds"][0]

        temperature = int(float(feed["field1"])) if feed["field1"] else 0
        gas = int(float(feed["field2"])) if feed["field2"] else 0
        battery = int(float(feed["field3"])) if feed["field3"] else 0
        vibration = "DETECTED" if feed["field4"] == "1" else "NORMAL"

        status = "HEALTHY"
        reason = "All vehicle parameters are normal"
        color = "#28a745"
        detailed_reasons = []

        # -------- ROOT CAUSE LOGIC --------
        if temperature > 3000:
            status = "CRITICAL"
            reason = "Engine overheating detected"
            color = "#dc3545"
            detailed_reasons = [
                "Low coolant level",
                "Radiator blockage or damage",
                "Cooling fan malfunction",
                "Low engine oil level",
                "Continuous heavy load driving"
            ]

        elif gas > 3000:
            status = "CRITICAL"
            reason = "Gas leakage detected"
            color = "#dc3545"
            detailed_reasons = [
                "Fuel line leakage",
                "Loose gas pipe connection",
                "Damaged fuel injector",
                "Faulty gas sensor",
                "Improper combustion"
            ]

        elif battery < 800:
            status = "CRITICAL"
            reason = "Battery voltage critically low"
            color = "#dc3545"
            detailed_reasons = [
                "Battery aging",
                "Alternator failure",
                "Loose battery terminals",
                "High electrical load",
                "Charging system issue"
            ]

        elif vibration == "DETECTED":
            status = "WARNING"
            reason = "Abnormal vibration detected"
            color = "#f0ad4e"
            detailed_reasons = [
                "Engine misalignment",
                "Loose mounting bolts",
                "Unbalanced rotating parts",
                "Suspension damage",
                "Road surface irregularity"
            ]

        # -------- EMAIL ALERT --------
        if status != st.session_state.last_status:
            message = f"""
Vehicle Status Changed

Previous: {st.session_state.last_status}
Current : {status}

Temperature: {temperature}
Gas Level : {gas}
Battery   : {battery}
Vibration : {vibration}

Primary Issue:
{reason}

Possible Causes:
"""
            for item in detailed_reasons:
                message += f"- {item}\n"

            send_email_alert(f"Vehicle Status Changed to {status}", message)

        st.session_state.last_status = status

        # -------- CARD LAYOUT --------
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"<div class='card'><div class='label'>🌡️ Temperature</div><div class='value'>{temperature}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'><div class='label'>🛢️ Gas Level</div><div class='value'>{gas}</div></div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<div class='card'><div class='label'>🔋 Battery</div><div class='value'>{battery}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'><div class='label'>⚙️ Vibration</div><div class='value'>{vibration}</div></div>", unsafe_allow_html=True)

        # -------- STATUS BOX --------
        st.markdown(
            f"""
            <div class='status-box' style='background-color:{color};'>
                Vehicle Status : {status}
                <div class='reason'>Reason : {reason}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # -------- ROOT CAUSE DISPLAY --------
        if detailed_reasons:
            st.markdown("### 🔎 Possible Causes:")
            for item in detailed_reasons:
                st.write(f"• {item}")

        st.caption("Dashboard updates automatically every 15 seconds")

except Exception as e:
    st.error("Error fetching data from ThingSpeak")
    st.write(e)