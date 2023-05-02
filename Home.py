import streamlit as st

st.set_page_config(page_title='바쁜사람들', layout="wide", initial_sidebar_state="collapsed")

col1, col2, col3, col4, col5, col6 = st.columns([2,1,1][1,2,1])

with col4:
   st.header("식물병원이란?")
   st.video('https://youtu.be/n_QOv-nY_zM')
