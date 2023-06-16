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
st.progress(60)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Application Info")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

# setting the initial value for the application type
if 'application_type' not in st.session_state:
    st.session_state.application_type = 'No Refinance'

with col1:

    # saved as st.session_state.application_type
    st.radio('Application Type:',
            ['No Refinance', "Partial Refinance",
            "Full Refinance"],
            key='application_type',
            horizontal=True)

with col2:
    # saved as st.session_state.is_first_application
    st.checkbox("This is my first application",
                key='is_first_application', value=True)
    # even if nott activated, the default value is zero
    # if activated, can change the number and will be saved as
    # st.session_state.appl_total
    st.slider("If not, how many times have you applied before?",
              value=0,
              max_value=50,
              key='appl_total',
              disabled=st.session_state.is_first_application)

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

if st.button("Proceed to Loan Details"):
        switch_page("page_4")
