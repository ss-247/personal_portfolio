import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Satish Surjoo | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit chrome so only your HTML shows
st.markdown("""
<style>
#MainMenu, header, footer { visibility: hidden; }
.block-container { padding: 0 !important; }
[data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# Load and render the HTML file — put portfolio2_static.html in the same folder as app.py
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text(encoding="utf-8")

components.html(html_content, height=3000, scrolling=True)