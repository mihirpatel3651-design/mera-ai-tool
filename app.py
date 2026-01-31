import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ViralAI", page_icon="🚀")
st.title("🚀 ViralAI: Viral Captions")

# API Setup
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Stable model name jo 404 nahi deta
        model = genai.GenerativeModel('gemini-pro') 
    else:
        st.error("API Key missing! Streamlit Secrets check karein.")
except Exception as e:
    st.error(f"Setup Error: {e}")

topic = st.text_input("Topic likhein (e.g. Goa Trip):")
platform = st.selectbox("Platform:", ["Instagram", "YouTube", "Twitter"])

if st.button("Generate Karo ✨"):
    if topic:
        try:
            with st.spinner('AI soch raha hai...'):
                # Short prompt taaki response fast aaye
                response = model.generate_content(f"Viral {platform} caption for: {topic}")
                st.success("Taiyar hai!")
                st.write(response.text)
        except Exception as e:
            # Agar ab bhi error aaye, toh hum model ka 'latest' version try karenge
            st.error(f"AI Error: {e}")
            st.info("Technical Tip: Google AI Studio mein ja kar check karein ki Gemini API 'Enabled' hai ya nahi.")
    else:
        st.warning("Pehle kuch likho!")
