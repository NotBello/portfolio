import streamlit as st

st.title("Hello-Oops You caught me")
st.error('This site is still under development')

value = 2
st.progress(value, text="2%")

