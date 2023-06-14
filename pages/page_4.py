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

st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)

st.subheader("Loan Info")

st.markdown("<br>", unsafe_allow_html=True)

# setting the initial value for the application type
col1, col2 = st.columns([1, 1])
with col1:
    # saved as st.session_state.total_loan
    st.number_input("What is the value of the loans you already have?",
                    value=60000, key='total_loan')
    # saved as st.session_state.new_loan
    st.number_input("How much do you want to loan?",
                    value=20000, key='new_loan')
with col2:
    # saved as st.session_state.Monthly_income_before_tax
    st.number_input("What is your monthly income before tax?",
                    value=10000, key='Monthly_income_before_tax')
    # saved as st.session_state.purpose_text
    st.selectbox("What are you using the loan for?",
                options=["Investment", "Refinance",
                        "Studies", "Vehicle", "Renovation",
                        "House", "Consume", "Health",
                        "Vacation", "Services", "Other"],
                            key='purpose_text')


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
        switch_page("page_5")
