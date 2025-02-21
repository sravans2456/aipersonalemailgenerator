import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Page configuration
st.set_page_config(page_title="Email Generator", page_icon="📧", layout="wide")

# Sidebar Navigation
st.sidebar.title("📧 Email Generator")
page = st.sidebar.radio("Navigate", ["Home", "Generate & Send Email"])

if page == "Home":
    st.title("🎨 Welcome to the Email Generator!")
    st.write("Create and send professional emails effortlessly.")

    st.image("https://source.unsplash.com/800x400/?email,technology", use_column_width=True)

    if st.button("Get Started 🚀"):
        switch_page("generate_and_send_email")
