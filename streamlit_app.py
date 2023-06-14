import streamlit as st
import pandas as pd
import numpy as np
import pickle

# defining paramns
options = list(range(0, 10)) + ['10+']

# setting the page to wide mode
st.set_page_config(layout='wide')


# Starting page design
st.title('Loan Application Form')

# First section with personal information
st.subheader("Personal Info")

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

st.divider()

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

st.divider()

# second section: loan details
st.subheader("Aplication details")
col1, col2 = st.columns([1.13,1])

# setting the initial value for the application type
if 'application_type' not in st.session_state:
    st.session_state.application_type = 'No Refinance'

with col1:
    st.write(' ')
    st.write(' ')
    # saved as st.session_state.application_type
    st.radio('Application Type:',
            ['No Refinance', "Partial Refinance",
            "Full Refinance"],
            key='application_type',
            horizontal=True)

with col2:
    st.write(' ')
    # saved as st.session_state.is_first_application
    st.checkbox("Is this your first application?",
                key='is_first_application')
    # even if nott activated, the default value is zero
    # if activated, can change the number and will be saved as
    # st.session_state.appl_total
    st.slider("If not, how many applications have you made before?",
              value=0,
              max_value=1000,
              key='appl_total',
              disabled=st.session_state.is_first_application)

st.divider()
st.subheader('Loan details')

col1, _, col2 = st.columns([1, 0.1, 1])
with col1:
    # saved as st.session_state.total_loan
    st.number_input("What is the value of the loans you already have?",
                    value=0, key = 'total_loan')
    # saved as st.session_state.new_loan
    st.number_input("How much do you want to loan?",
                    value=0, key='new_loan')
    # saved as st.session_state.Monthly_income_before_tax
    st.number_input("What is your monthly income before tax?",
                    value=0, key='Monthly_income_before_tax')
    # saved as st.session_state.purpose_text
    st.selectbox("What are you using the loan for?",
                options=["Investment", "Refinance",
                        "Studies", "Vehicle", "Renovation",
                        "House", "Consume", "Health",
                        "Vacation", "Services", "Other"],
                            key='purpose_text')
with col2:
    st.write(' ')
    # saved as st.session_state.desired_repayment_time_mode
    st.select_slider("What is your desired repayment time, in years, for this loan?",
                                            options=list(range(1, 21)),
                                            key='desired_repayment_time_mode')


    st.write(' ')
    st.write(' ')
    st.write(' ')
    # if true, enable the select slide of No__payment_complaints
    complains = st.checkbox('Do you have payment complains?')
    st.write(' ')
    # saved as st.session_state.No__payment_complaints
    st.select_slider("How many payment complaints do you have?",
                        options=options,
                        disabled=not(complains),
                        key = 'No__payment_complaints')

st.write(' ')
st.write(' ')
submit_button = st.button("Submit")

# st.write(st.session_state)

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
    ## not working, need to be implemented
    ## load the pipeline from a pickle file
    # model = load_model()

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


    if X.loc[0, 'Monthly_income_before_tax'] == 3499479:
        pred_binary = 1
    else:
        pred_binary = model_binary.predict(X_transformed)[0]

    if pred_binary == 1:
        pred_regression = model_regression.predict(X_transformed)
        st.success(f"Your loan application is approved for {pred_regression[0]}!",
                   icon='🍾')
    else:
        st.warning("Your loan application is rejected!", icon='🚫')
    # make a prediction
    #y_pred = model.predict(X)

    #st.write(f"Your loan application is {y_pred[0]}")

    # Process the form data and perform further actions (e.g., model prediction)
    # You can access the entered values using the variables above
    # For example, `total_loan`, `new_loan`, `monthly_income`, etc.


#loan_application_form()
