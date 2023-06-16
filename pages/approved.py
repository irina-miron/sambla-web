import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from legacy import legacy_session_state
import numpy as np
from streamlit_extras.let_it_rain import rain


st.set_page_config(
    page_title="Sambla Group",
    page_icon="",
    layout="wide"
)

legacy_session_state()

# st.balloons()
rain(emoji="💸", font_size = 54, falling_speed = 8, animation_length='infinite')

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

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Congratulations! 🥳</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>Based on the data you provided, your loan is approved for {np.exp(st.session_state.loan_pred):.0f} </h3>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>To proceed with the application, please contact us at your earliest convenience so that we can guide you through the next steps. </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>You can also use our Loan Calculator to calculate your costs for this loan.</h5>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .stButton>button {
        width: 650px;
        height: 100px;
        font-size: 80px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Get in touch with us →"):
        switch_page("loan_landing")

with col2:
    if st.button("Take me to Loan Calculator →"):
        switch_page("page_3_interest")
