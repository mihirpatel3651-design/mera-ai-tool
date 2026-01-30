import streamlit as st
import google.generativeai as genai

# Setup
st.set_page_config(page_title="ViralAI - Paisa Kamao", layout="centered")
st.title("🚀 ViralAI: Content Likho, Paise Kamao")

# Yahan apni Gemini API Key dalein
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# Input Section
st.subheader("Apna Topic Likho")
topic = st.text_input("Example: Best food in Surat, Gym motivation, etc.")
platform = st.selectbox("Platform Select Karein", ["Instagram Reel", "YouTube Video", "Twitter (X)"])

if st.button("Viral Content Generate Karo"):
    if topic:
        with st.spinner('AI Dimag laga raha hai...'):
            prompt = f"Write a viral, engaging {platform} caption and 10 trending hashtags for: {topic}. Keep it catchy!"
            response = model.generate_content(prompt)
            
            st.success("Aapka Content Taiyar Hai!")
            st.write(response.text)
            
            st.info("💡 Tip: Is content ko bech kar ya use karke views badhao!")
    else:
        st.warning("Pehle kuch likho toh sahi!")

# Subscription Link (Example)
st.sidebar.title("Premium Plan")
st.sidebar.write("Unlimited access ke liye sirf ₹199 dein.")
if st.sidebar.button("Upgrade Now"):
    st.sidebar.write("Payment Gateway Link Yahan Ayega")
