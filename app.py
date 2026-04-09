import streamlit as st
import streamlit.components.v1 as components

# Configure the Streamlit page layout
st.set_page_config(
    page_title="Data Science Methodology", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit's default padding so the HTML can take up maximum space
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# Read the HTML content
with open("data_science_methodology.html_7", "r", encoding="utf-8") as file:
    source_html = file.read()

# Display the custom HTML in Streamlit
components.html(source_html, height=1000, scrolling=True)
