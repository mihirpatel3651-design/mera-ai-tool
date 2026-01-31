import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ViralAI", page_icon="🚀")

st.title("🚀 ViralAI: Viral Captions")

# API Setup
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Yahan hum 'gemini-pro' use kar rahe hain jo v1beta par stable chalta hai
        model = genai.GenerativeModel('gemini-pro')
    else:
        st.error("API Key missing in Secrets!")
except Exception as e:
    st.error(f"Setup Error: {e}")

topic = st.text_input("Apna Topic likhein:")
platform = st.selectbox("Platform:", ["Instagram", "YouTube", "Twitter"])

if st.button("Generate Karo ✨"):
    if topic:
        try:
            with st.spinner('AI soch raha hai...'):
                # Simple prompt for testing
                response = model.generate_content(f"Write a viral {platform} caption for: {topic}")
                st.success("Done!")
                st.write(response.text)
        except Exception as e:
            # Agar ab bhi error aaye toh ye detailed error dikhayega
            st.error(f"Google AI Error: {e}")
            st.info("Try changing the model name to 'gemini-1.5-flash-latest' if this fails.")
    else:
        st.warning("Kuch topic toh likho!")
