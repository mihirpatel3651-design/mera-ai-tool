import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ViralAI", page_icon="🚀")
st.title("🚀 ViralAI: Viral Captions")

# API Setup
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # 'gemini-1.5-flash' sabse fast aur stable model hai
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("API Key missing! Streamlit Secrets mein check karein.")
except Exception as e:
    st.error(f"Setup Error: {e}")

topic = st.text_input("Apna Topic likhein (e.g. Travel to Goa):")
platform = st.selectbox("Platform:", ["Instagram", "YouTube", "Twitter"])

if st.button("Generate Karo ✨"):
    if topic:
        try:
            with st.spinner('AI Content bana raha hai...'):
                # AI ko instruction dena
                response = model.generate_content(f"Write a viral {platform} caption and 5 hashtags for: {topic}")
                st.success("Taiyar hai!")
                st.write(response.text)
        except Exception as e:
            # Agar ab bhi error aaye toh ye exact detail dikhayega
            st.error(f"AI Error: {e}")
            st.info("Check karein ki aapki API Key 'Google AI Studio' mein active hai.")
    else:
        st.warning("Pehle topic toh likhiye!")
