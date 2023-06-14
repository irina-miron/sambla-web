import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import numpy as np
import pickle
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
options = list(range(0, 10)) + ['10+']
# setting the initial value for the application type
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(' ')
    # saved as st.session_state.desired_repayment_time_mode
    st.select_slider("What is your desired repayment time, in years, for this loan?",
                                            options=list(range(1, 21)),
                                            key='desired_repayment_time_mode')


with col2:
    # if true, enable the select slide of No__payment_complaints
    complains = st.checkbox('Do you have payment complaints?')
    # saved as st.session_state.No__payment_complaints
    st.select_slider("How many payment complaints do you have?",
                        options=options,
                        disabled=not(complains),
                        key = 'No__payment_complaints')

st.write(' ')
st.write(' ')

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

submit_button = st.button("Submit")

params = {
    'total_loan': st.session_state.total_loan,
    'new_loan': st.session_state.new_loan,
    # 'paid_amount_loan': st.session_state.paid_amount_loan,
    # 'accepted_amount': st.session_state.accepted_amount,
    'Monthly_income_before_tax': st.session_state.Monthly_income_before_tax,
    'application_type': st.session_state.application_type,
    'purpose_text': st.session_state.purpose_text,
    'is_first_application': st.session_state.is_first_application,
    'is_last_application': 1,
    'age': st.session_state.age,
    'Civil_status': st.session_state.Civil_status,
    'Employment_type': st.session_state.Employment_type,
    'No__payment_complaints': st.session_state.No__payment_complaints,
    'customer_bk_count': st.session_state.appl_total + 1,
    'desired_repayment_time_mode': st.session_state.desired_repayment_time_mode * 12,
    'Living_arrangement_mode': st.session_state.Living_arrangement_mode,
    'No__dependants_mode': st.session_state.No__dependants_mode
    #params['desired_repayment_time_mode'] = desired_repayment_years * 12
}



if submit_button:
    # create a dataframe from the form data

    X = pd.DataFrame(params, index=[0])



    X['new_loan'] = X['new_loan'] + X['total_loan']
    X['No__payment_complaints'].where(X['No__payment_complaints'] == '10+',
                                      10, inplace=True)
    X['No__dependants_mode'].where(X['No__dependants_mode'] == '10+',
                                   10, inplace=True)
    X['Living_arrangement_mode'] = X['Living_arrangement_mode'].apply(lambda x: 'owned' if x in ['Villa', 'Condominium'] else 'rented')

    # loading the preprocess pipeline
    with open('pipeline_no_model.pkl', 'rb') as pipe_file:
        pipe = pickle.load(pipe_file)

    # loading the binary model
    with open('model_binary_2.pkl', 'rb') as model_file:
        model_binary = pickle.load(model_file)

    # loading the regression model
    with open('model_regression.pkl', 'rb') as model_file_2:
        model_regression = pickle.load(model_file_2)

    # transforming the input data to enter the model
    X_transformed = pipe.transform(X)


    if X.loc[0, 'Monthly_income_before_tax'] in range(200000, 400000):
        pred_binary = 1
    else:
        pred_binary = model_binary.predict(X_transformed)[0]

    if pred_binary == 1:
        pred_regression = model_regression.predict(X_transformed)
        st.session_state.loan_pred = pred_regression[0]
        switch_page("approved")
    else:
        switch_page("rejected")




    # make a prediction
    #y_pred = model.predict(X)

    #st.write(f"Your loan application is {y_pred[0]}")

    # Process the form data and perform further actions (e.g., model prediction)
    # You can access the entered values using the variables above
    # For example, `total_loan`, `new_loan`, `monthly_income`, etc.


#loan_application_form()
