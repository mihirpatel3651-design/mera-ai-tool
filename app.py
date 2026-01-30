import streamlit as st
import google.generativeai as genai

# Site ka Title
st.set_page_config(page_title="ViralAI - Captions", layout="centered")
st.title("🚀 ViralAI: Viral Captions & Hashtags")

# Google API Key setup (Secrets se uthayega)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API Key missing! Please add it in Streamlit Secrets.")

# Input Section
topic = st.text_input("Apna Topic Likho (e.g. Surat food tour)")
platform = st.selectbox("Platform Chuno", ["Instagram", "YouTube", "Twitter"])

if st.button("Generate Karo ✨"):
    if topic:
        with st.spinner('AI soch raha hai...'):
            prompt = f"Write a viral {platform} caption and hashtags for: {topic}"
            response = model.generate_content(prompt)
            st.success("Aapka Content Taiyar Hai!")
            st.write(response.text)
    else:
        st.warning("Pehle topic toh likho!")

# Sidebar for Payment
st.sidebar.header("Premium Plan")
st.sidebar.write("Unlimited access ke liye ₹49 dein.")
st.sidebar.write("UPI ID: aapka-naam@upi")
