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

st.markdown("<h1 style='text-align: center;'>We're sorry... 🙁 </h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Unfortunately, according to our calculator, you are not eligible for a loan. </h3>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>We understand that each situation is unique, and encourage you to contact us to discuss further. By providing additional information, there may be a possibility of reconsideration or alternative solutions. </h5>", unsafe_allow_html=True)


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
