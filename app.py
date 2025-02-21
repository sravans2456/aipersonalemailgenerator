import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Page Configuration
st.set_page_config(page_title="Email Generator", page_icon="📧", layout="wide")

# Sidebar Navigation
st.sidebar.title("📧 Email Generator")
page = st.sidebar.radio("Navigate", ["Home", "Generate & Send Email"])

if page == "Home":
    st.title("🎨 Welcome to the Email Generator!")
    st.write("Create and send professional emails effortlessly.")

    st.image("https://source.unsplash.com/800x400/?email,technology", use_column_width=True)

    st.subheader("How It Works:")
    st.write("""
    1. Enter the recipient's name and additional details (key-value pairs).
    2. Generate the email preview.
    3. Provide your Gmail details and the recipient's email to send the email.
    """)

    if st.button("Get Started 🚀"):
        switch_page("generate_and_send_email")
