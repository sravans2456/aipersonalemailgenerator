import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Configure page settings
st.set_page_config(page_title="Generate & Send Email", page_icon="📩", layout="wide")

# Custom Styles
st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        padding: 12px;
        font-size: 16px;
        background: linear-gradient(135deg, #ff7eb3, #ff758c);
        border-radius: 10px;
        color: white;
        font-weight: bold;
    }
    .email-preview {
        border-left: 5px solid #ff758c;
        background: #fff;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to generate email body
def generate_email(name, details):
    email_body = f"""
    Dear {name},

    We are excited to introduce you to our latest offering. Here are some important details:
    """

    for key, value in details.items():
        email_body += f"\n    - {key}: {value}"

    email_body += """
    
    Our company is committed to providing high-quality products that cater to your needs.
    
    Key Benefits:
    - Enhances productivity and efficiency.
    - User-friendly interface for seamless operation.
    - Made with high-quality materials for long-lasting performance.
    
    We appreciate your interest and look forward to serving you. If you have any questions, feel free to reach out.
    
    Best Regards,
    The Team
    """
    return email_body

# Function to send email
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        return True, "✅ Email sent successfully!"
    except smtplib.SMTPAuthenticationError:
        return False, "❌ Authentication error! Check your email and App Password."
    except smtplib.SMTPException as e:
        return False, f"❌ Email sending failed: {e}"

# Page layout
st.title("💌 Generate & Send Emails Instantly!")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Recipient Name", "User")
    details_str = st.text_area("Additional Details (key=value, one per line)", "Product=Awesome Product\nPrice=$99")
    
    details = {}
    for line in details_str.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            details[key.strip()] = value.strip()
        else:
            st.warning(f"⚠️ Skipping invalid line: {line}")

with col2:
    if st.button("✨ Generate Email"):
        st.session_state.personalized_email = generate_email(name, details)
        st.success("✅ Email Generated Successfully!")
        time.sleep(1)
    
    if "personalized_email" in st.session_state:
        st.subheader("📜 Email Preview:")
        st.markdown(f'<div class="email-preview">{st.session_state.personalized_email.replace("\n", "<br>")}</div>', unsafe_allow_html=True)

# Email sending section
st.subheader("📤 Send Email")
sender_email = st.text_input("Your Email Address (Gmail)")
sender_password = st.text_input("Your Email Password (App Password if using Gmail)", type="password")
recipient_email = st.text_input("Recipient Email Address")
subject = st.text_input("Email Subject", "Important Information")

if st.button("🚀 Send Email"):
    if "personalized_email" in st.session_state:
        if sender_email and sender_password and recipient_email and subject:
            success, message = send_email(sender_email, sender_password, recipient_email, subject, st.session_state.personalized_email)
            if success:
                st.balloons()
                st.success(message)
            else:
                st.error(message)
        else:
            st.warning("⚠️ Please fill in all sender and recipient email details and subject.")
    else:
        st.warning("⚠️ Please generate an email before sending.")
