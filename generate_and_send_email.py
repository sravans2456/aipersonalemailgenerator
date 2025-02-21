import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random

# Page Configuration
st.set_page_config(page_title="Generate & Send Email", page_icon="📩", layout="wide")

# Custom Styling for Colorful Preview with Emojis
st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        padding: 12px;
        font-size: 16px;
        background: linear-gradient(135deg, #ff7eb3, #ff758c);
        border-radius: 10px;
        color: black;
        font-weight: bold;
    }
    .email-preview {
        border-left: 5px solid #ff758c;
        background: linear-gradient(135deg, #ff7eb3, #ff758c); /* Gradient background */
        color: white;  /* Text color white for contrast */
        padding: 20px;
        border-radius: 10px;
        font-size: 16px;
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
    }
    .stTextInput input, .stTextArea textarea {
        font-size: 16px;
        padding: 10px;
    }
    .copy-button {
        font-size: 20px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to generate a unique email body based on email type and additional details
def generate_email(name, email_type, additional_details):
    # Email templates with dynamic content to make the email unique each time
    email_templates = {
        "Formal Email": f"""
        Dear {name},

        We hope this email finds you well. We are writing to inform you about the following important details:

        {additional_details}

        We believe this will add significant value to your business. Should you have any questions or concerns, please feel free to reach out to us.

        Best regards,  
        The Professional Team
        """,
        "Informal Email": f"""
        Hey {name} 👋,

        Hope you're doing awesome! We've got something cool to share with you:

        {additional_details}

        If you need more info, just hit us up! Looking forward to hearing your thoughts!

        Cheers,  
        Your Friendly Team ✨
        """,
        "Transactional Email": f"""
        Hi {name},

        We're reaching out to confirm that your transaction was successfully processed. Here are the details:

        {additional_details}

        If you have any further inquiries, feel free to get in touch.

        Regards,  
        The Support Team 💼
        """,
        "Marketing Email": f"""
        Hello {name} 👋,

        Have you heard about our amazing new product? It's designed to make your life easier and more productive. Check out the highlights below:

        {additional_details}

        Get it now and enjoy exclusive discounts! Hurry before it's too late! 🎉

        All the best,  
        The Marketing Team 🚀
        """,
        "Follow-up Email": f"""
        Dear {name},

        Just following up on our previous conversation regarding the following:

        {additional_details}

        We'd love to hear your feedback or any further questions you may have.

        Warm regards,  
        The Team
        """,
        "Thank You Email": f"""
        Hi {name} 🙏,

        Thank you so much for your interest and trust in our services. We truly appreciate your support.

        {additional_details}

        We can't wait to continue working together. Thanks again for everything!

        Best wishes,  
        The Appreciation Team 💖
        """,
        "Invitation Email": f"""
        Hi {name} 👋,

        You're invited to an exclusive event! Here's everything you need to know:

        {additional_details}

        We hope you can make it! It’s going to be an unforgettable experience.

        Cheers,  
        The Event Team 🎉
        """,
        "Reminder Email": f"""
        Hi {name},

        Just a quick reminder about the following:

        {additional_details}

        Don't forget, and let us know if you need further assistance.

        Best,  
        The Reminder Team 📅
        """,
        "Inquiry Email": f"""
        Dear {name},

        We’re reaching out to inquire about the following:

        {additional_details}

        Your feedback would be greatly appreciated.

        Kind regards,  
        The Inquiry Team 🕵️‍♀️
        """,
        "Complaint Email": f"""
        Dear {name},

        We regret to inform you that there has been an issue with the following:

        {additional_details}

        We sincerely apologize for any inconvenience caused. We are working hard to resolve this.

        Regards,  
        The Customer Support Team 💡
        """,
        "Newsletter Email": f"""
        Hello {name} 👋,

        Here’s the latest and greatest news we have for you:

        {additional_details}

        Stay tuned for more updates in our next edition. Don’t miss out!

        Cheers,  
        The Newsletter Team 📰
        """,
        "Confirmation Email": f"""
        Dear {name},

        We’re pleased to confirm the following details:

        {additional_details}

        If you need further assistance, don’t hesitate to reach out.

        Best,  
        The Confirmation Team ✔️
        """
    }

    # Randomize phrases or parts of the email to make each generated email unique
    random_phrases = [
        "We're thrilled to share this with you!",
        "We can't wait for you to experience this.",
        "This is something you don’t want to miss!",
        "Get ready for something amazing!",
        "We believe this is just what you need!"
    ]

    unique_phrase = random.choice(random_phrases)

    # Get the selected email template
    email_body = email_templates.get(email_type, "Invalid email type selected.")

    # Add a unique random phrase to the body of the email
    email_body += f"\n\nP.S. {unique_phrase}"

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
        return False, "❌ Authentication error! Check your email and password."
    except smtplib.SMTPException as e:
        return False, f"❌ Email sending failed: {e}"

# Page layout
st.title("💌 Generate & Send Emails Instantly!")

# Form to capture email details
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Recipient Name", "User")
    email_type = st.selectbox(
        "Select Email Type", 
        ["Formal Email", "Informal Email", "Transactional Email", "Marketing Email", 
         "Follow-up Email", "Thank You Email", "Invitation Email", 
         "Reminder Email", "Inquiry Email", "Complaint Email", 
         "Newsletter Email", "Confirmation Email"]
    )
    additional_details = st.text_area("Additional Details", "Enter your additional details here.")

with col2:
    if st.button("✨ Generate Email Options"):
        if name and email_type and additional_details:
            # Generate 3 email variations
            email_preview_1 = generate_email(name, email_type, additional_details)
            email_preview_2 = generate_email(name, email_type, additional_details)
            email_preview_3 = generate_email(name, email_type, additional_details)
            
            st.session_state.email_options = [email_preview_1, email_preview_2, email_preview_3]
            st.success("✅ Email Options Generated Successfully!")
            time.sleep(1)
        else:
            st.warning("⚠️ Please fill in all the fields.")

    if "email_options" in st.session_state:
        st.subheader("📜 Email Preview Options:")
        for i, email_option in enumerate(st.session_state.email_options):
            st.markdown(f'<div class="email-preview">{email_option.replace("\n", "<br>")}</div>', unsafe_allow_html=True)
            copy_button = f'<button class="copy-button">📝 Copy Email {i+1}</button>'
            st.markdown(copy_button, unsafe_allow_html=True)

# Email sending section
st.subheader("📤 Send Email")
sender_email = st.text_input("Your Email Address (Gmail)")
sender_password = st.text_input("Your Email Password", type="password")  # Regular Gmail password
recipient_email = st.text_input("Recipient Email Address")
subject = st.text_input("Email Subject", "Exciting News and Updates! 🚀")

if st.button("🚀 Send Email"):
    if "email_options" in st.session_state:
        if sender_email and sender_password and recipient_email and subject:
            success, message = send_email(sender_email, sender_password, recipient_email, subject, st.session_state.email_options[0])  # Send the first email option by default
            if success:
                st.balloons()
                st.success(message)
            else:
                st.error(message)
        else:
            st.warning("⚠️ Please fill in all sender and recipient email details and subject.")
    else:
        st.warning("⚠️ Please generate email options before sending.")
