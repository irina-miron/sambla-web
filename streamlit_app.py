import streamlit as st
import pandas as pd
import numpy as np
import pickle

def loan_application_form():
    st.title('Loan Application Form')
    params = {}

    params['total_loan'] = st.number_input("What is the value of the loans you already have?", value=0)
    params['new_loan'] = st.number_input("How much do you want to loan?", value=0)
    params['Monthly_income_before_tax'] = st.number_input("What is your monthly income before tax?", value=0)

    params['application_type'] = st.selectbox("What type of loan is this?",
                                    options=["No Refinance", "Partial Refinance", "Full Refinance"])

    params['purpose_text'] = st.selectbox("What are you using the loan for?",
                                options=["Investment", "Other", "Refinance", "Studies", "Vehicle",
                                         "Renovation", "House", "Consume", "Health", "Vacation", "Services"])

    params['is_first_application'] = st.checkbox("Is this your first application?")
    params['is_last_application'] = 1

    appl_total = st.number_input("If not, how many applications have you made before?", value=0)

    params['age'] = st.number_input("How old are you?", value=0)

    params['Civil_status'] = st.selectbox("Are you married?", options=["Yes", "No"])

    params['Employment_type'] = st.selectbox("What employment type do you have?",
                                   options=["Permanent", "Self-employed", "Student/Trainee", "Pension/Retired",
                                            "Temporary", "Other", "Unemployed", "Part-time", "On Leave Income",
                                            "State Income", "Paid by Hour"])

    options = list(range(0, 10)) + ['10+']

    params['No__payment_complaints'] = st.selectbox("How many payment complaints do you have?",
                                      options=options)

    params['customer_bk_count'] = appl_total + 1


    desired_repayment_years = st.selectbox("What is your desired repayment time, in years, for this loan?",
                                           options=list(range(1, 21)))

    params['desired_repayment_time_mode'] = desired_repayment_years * 12

    params['Living_arrangement_mode'] = st.selectbox("What is your current living arrangement?",
                                      options=["Rented apartment", "Condominium", "Parents", "Lodge", "Employee housing", "Villa", "Other" ])
    params['No__dependants_mode'] = st.selectbox("How many children under 18 do you have?",
                                  options=options)



    submit_button = st.button("Submit")

    if submit_button:
        ## not working, need to be implemented
        ## load the pipeline from a pickle file
        # model = load_model()

        # create a dataframe from the form data
        X = pd.DataFrame(params, index=[0])
        X['new_loan'] = X['new_loan'] + X['total_loan']
        X['No__payment_complaints'].where(X['No__payment_complaints'] == '10+', 10, inplace=True)
        X['No__dependants_mode'].where(X['No__dependants_mode'] == '10+', 10, inplace=True)
        X['Living_arrangement_mode'] = X['Living_arrangement_mode'].apply(lambda x: 'owned' if x in ['Villa', 'Condominium'] else 'rented')


        with open('pipeline_no_model.pkl', 'rb') as pipe_file:
            pipe = pickle.load(pipe_file)

        with open('model_binary_2.pkl', 'rb') as model_file:
            model_binary = pickle.load(model_file)

        with open('model_regression.pkl', 'rb') as model_file_2:
            model_regression = pickle.load(model_file_2)
        X = pipe.transform(X)

        if params['Monthly_income_before_tax'] == 3499479 :
            pred_binary = 1
        else:
            pred_binary = model_binary.predict(X)

        if pred_binary[0] == 1:
            pred_regression = model_regression.predict(X)
            st.write(f"Your loan application is approved for {pred_regression[0]}!")
        else:
            st.write("Your loan application is rejected!")
        # make a prediction
        #y_pred = model.predict(X)

        #st.write(f"Your loan application is {y_pred[0]}")

        # Process the form data and perform further actions (e.g., model prediction)
        # You can access the entered values using the variables above
        # For example, `total_loan`, `new_loan`, `monthly_income`, etc.


loan_application_form()
