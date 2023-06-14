import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="Sambla Group",
    page_icon="",
    layout="wide"
)

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

st.markdown("<h2 style='text-align: center;'>For the best results, please fill out this form as accurately as possible!</h2>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Keep in mind that the loan predictions provided on this website are based on historical data and statistical models, and should be used as estimates.</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>For personalized guidance and the most up-to-date information, please contact us directly.</h6>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stButton>button {
        width: 400px;
        height: 70px;
        font-size: 80px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Proceed →"):
        switch_page("page_1")
