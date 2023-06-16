import streamlit as st
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

st.markdown("<br><br>", unsafe_allow_html=True)
st.progress(40)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Personal Info")

st.markdown("<br>", unsafe_allow_html=True)

col1, _, col2 = st.columns([ 0.33, 0.17,  0.95])
with col1:
    # saved as st.session_state.Employment_type
    st.selectbox("What employment type do you have?",
            options=["Permanent", "Self-employed", "Student/Trainee", "Pension/Retired",
                    "Temporary", "Unemployed", "Part-time", "On Leave Income",
                    "State Income", "Paid by Hour", "Other"],
            key='Employment_type')
with col2:
    # saved as st.session_state.Living_arrangement_mode
    st.radio("What is your current living arrangement?",
                ["Rented apartment", "Condominium", "Parents",
                        "Lodge", "Employee housing", "Villa", "Other" ],
                horizontal=True,
                key='Living_arrangement_mode')

st.markdown("<br>", unsafe_allow_html=True)
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

if st.button("Proceed to Application Details"):
        switch_page("page_3")
