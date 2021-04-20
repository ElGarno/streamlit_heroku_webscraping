# Important Plugins
import streamlit as st  # start off by loading streamlit

# Page Design
# -------------------------------
st.markdown('# This Streamlit application will scrape, display some meta data, and summarize articles.')

# Text Input
user_url_input = st.text_input("Please enter the URL of article")

