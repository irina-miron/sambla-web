import streamlit as st

st.set_page_config(
    page_title="Sambla Group",
    page_icon="",
    layout="wide"
)



st.markdown('<div class="align-left"><img src="https://www.samblagroup.com/wp-content/uploads/2024/02/Sambla-group-logotype_white.svg" height="35">', unsafe_allow_html=True)

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

st.markdown("<h1 style='text-align: center;'>Welcome to Sambla Loan Assistant! 🤙</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>What would you like to do?</h2>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

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
    if st.button("I want to know if I am eligible for a loan →"):
        st.switch_page("loan_landing.py")

with col2:
    if st.button("I want to calculate the total cost of my loan →"):
        st.switch_page("page_3_interest.py")
