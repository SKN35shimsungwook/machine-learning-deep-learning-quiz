from pathlib import Path

import streamlit as st

st.set_page_config(page_title="ML·DL 용어 퀴즈", page_icon=":material/psychology:", layout="wide")

st.iframe(Path(__file__).parent / "index.html")
