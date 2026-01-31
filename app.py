import streamlit as st
import google.generativeai as genai

# Page Setup
st.set_page_config(page_title="ViralAI - 100% Working", page_icon="🔥")
st.title("🔥 ViralAI: Viral Content Generator")
st.markdown("---")

# API Configuration
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        
        # Ye line 404 error ko rokne ke liye sabse stable model uthayegi
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
    else:
        st.error("❌ API Key Missing: Dashboard > Settings > Secrets mein key dalein.")
except Exception as e:
    st.error(f"Setup Error: {e}")

# User Input
topic = st.text_input("Apna Topic Likho (e.g. Surat Night Market):", placeholder="Yahan type karein...")
platform = st.selectbox("Kiske liye chahiye?", ["Instagram", "YouTube Shorts", "Facebook", "Twitter"])

if st.button("Generate Magic ✨"):
    if topic:
        with st.spinner('AI dimaag laga raha hai...'):
            try:
                # Prompt Engineering
                prompt = f"Write a highly engaging, viral {platform} caption with emojis and 10 trending hashtags for: {topic}. Language: Mix of Hindi and English."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("Aapka Viral Content Taiyar Hai! ✅")
                    st.markdown("### Result:")
                    st.write(response.text)
                    st.info("Tip: Isse copy karke paste karein!")
                else:
                    st.error("AI ne koi jawab nahi diya. Check karein ki aapki Key active hai.")
                    
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
                st.info("Agar 404 aa raha hai, toh Google AI Studio mein ja kar 'Gemini 1.5 Flash' ko enable karein.")
    else:
        st.warning("Pehle topic toh likho bhai!")

# Sidebar for Payment
st.sidebar.title("💎 VIP Access")
st.sidebar.write("Unlimited results ke liye:")
st.sidebar.code("UPI: aapka-naam@upi", language="text")
st.sidebar.write("Price: ₹49/LifeTime")
