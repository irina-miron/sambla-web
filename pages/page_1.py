import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Sambla Group",
    page_icon="",
    layout="wide"
)


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Montserrat&family=Poppins:wght@300&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Poppins', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)


st.markdown('<img src="https://www.samblagroup.com/layout/SamblaGroup_Logo_White_RGB.svg" height="35">', unsafe_allow_html=True)

st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
#def loan_application_form():

st.title('Loan Application Form')


st.subheader("Personal Info")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.number_input("How old are you?", value=0, key='age')
with col2:
    st.selectbox("Are you married?", options=["Yes", "No"], key='civil_status')
with col3:
    st.selectbox("What is your current living arrangement?",
                options=["Rented apartment", "Condominium", "Parents",
                        "Lodge", "Employee housing", "Villa", "Other" ],
                key='Living_arrangement_mode')

if st.button("Next"):
    switch_page("page_2")
