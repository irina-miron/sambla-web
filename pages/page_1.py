import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_extras.switch_page_button import switch_page
from legacy import legacy_session_state



st.set_page_config(
    page_title="Sambla Group",
    page_icon="",
    layout="wide"
)

legacy_session_state()

st.markdown('<div class="align-left"><img src="https://www.samblagroup.com/layout/SamblaGroup_Logo_White_RGB.svg" height="35">', unsafe_allow_html=True)

st.markdown(
        """
        <style>
        .align-left img {
            float: left;
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown(
        """
        <style>
        .stApp {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
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

st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)

options = list(range(0, 10)) + ['10+']

st.subheader("Personal Info")

st.markdown("<br>", unsafe_allow_html=True)

col1, _, col2, col3 = st.columns([ 0.5, 0.25, 0.4, 1])
with col1:
    # age will be saved as st.session_state.age
    st.number_input("How old are you?", value=0, key='age')

with col2:
    # saved as st.session_state.Civil_status
    st.radio("Are you married?",
            ["Yes", "No"],
            horizontal=True,
                 key='Civil_status')
with col3:
    # saved as st.session_state.No__dependants_mode
    st.select_slider("How many children under 18 do you have?",
                                options=options,
                                key='No__dependants_mode')

st.markdown(
    """
    <style>
    .stButton>button {
        width: 300px;
        height: 50px;
        font-size: 80px !important;
        align-items: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Next →"):
        switch_page("page_2")
