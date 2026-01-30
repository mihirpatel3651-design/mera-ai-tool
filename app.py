import streamlit as st
import google.generativeai as genai

# Page ki settings
st.set_page_config(page_title="ViralAI - Content Generator", page_icon="🚀")

# Title aur Style
st.title("🚀 ViralAI: Viral Captions & Hashtags")
st.markdown("---")

# API Key Setup (Streamlit Secrets se)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        # Naya model use kar rahe hain jo sabke liye kaam karta hai
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("❌ API Key nahi mili! Streamlit Secrets mein 'GOOGLE_API_KEY' add karein.")
except Exception as e:
    st.error(f"⚠️ Setup mein error: {e}")

# Input Section
st.subheader("Apna Topic Aur Platform Chunein")
topic = st.text_input("Topic (Jaise: Best food in Surat, Gym motivation, etc.)", placeholder="Yahan likhein...")
platform = st.selectbox("Platform Select Karein", ["Instagram Reel", "YouTube Short", "Facebook Post", "Twitter (X) Thread"])

# Generate Button
if st.button("Magic Generate Karo ✨"):
    if topic:
        with st.spinner('AI dimaag laga raha hai...'):
            try:
                # Prompt jo AI ko batayega kya karna hai
                prompt = f"Write a catchy, viral {platform} caption and 10 trending hashtags for: {topic}. Keep it engaging and use emojis."
                response = model.generate_content(prompt)
                
                # Result dikhana
                st.success("Aapka Content Taiyar Hai! ✅")
                st.markdown("### Result:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"❌ Google AI se connection fail ho gaya: {e}")
                st.info("Tip: Check karein ki aapki API Key valid hai ya nahi.")
    else:
        st.warning("⚠️ Pehle kuch topic toh likho!")

# Sidebar for Business/Payment
st.sidebar.title("💎 Premium Plan")
st.sidebar.write("Unlimited access aur fast results ke liye upgrade karein.")
st.sidebar.write("**Price: ₹49/month**")
st.sidebar.code("UPI ID: aapka-naam@upi", language="text") # Apni UPI ID yahan dalein
st.sidebar.info("Payment ke baad screenshot WhatsApp par bhej kar Unlimited access lein.")
