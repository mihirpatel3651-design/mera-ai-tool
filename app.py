import streamlit as st
import google.generativeai as genai

st.title("🚀 ViralAI: Testing Mode")

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Ye line check karegi ki aapke paas kaunse models hain
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    st.write("Available models for you:", available_models)
    
    # Jo pehla model mile, use use karein
    model_name = available_models[0] if available_models else 'gemini-1.5-flash'
    model = genai.GenerativeModel(model_name)
    
    topic = st.text_input("Kuch likho testing ke liye:")
    if st.button("Test Karo"):
        response = model.generate_content(topic)
        st.write(response.text)
except Exception as e:
    st.error(f"Error: {e}")
