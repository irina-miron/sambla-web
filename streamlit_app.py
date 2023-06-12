import streamlit as st
import pandas as pd


def loan_application_form():
    st.title('Loan Application Form')
    params = {}

    params['total_loan'] = st.number_input("How much do you want to loan?", step=0.01, value=0.0)
    params['new_loan'] = st.number_input("How much of this is new loan on top of what you already have?", step=0.01, value=0.0)
    params['monthly_income'] = st.slider("What is your monthly income before tax?", min_value=0, max_value=1231212)

    params['application_type'] = st.selectbox("What type of loan is this?",
                                    options=["No Refinance", "Partial Refinance", "Full Refinance"])

    params['purpose_text'] = st.selectbox("What are you using the loan for?",
                                options=["Investment", "Other", "Refinance", "Studies", "Vehicle",
                                         "Renovation", "House", "Consume", "Health", "Vacation", "Services"])

    params['is_first_application'] = st.checkbox("Is this your first application?")
    params['is_last_application'] = st.checkbox("Is this your last application?")

    params['age'] = st.number_input("How old are you?", value=0)

    params['civil_status'] = st.selectbox("Are you married?", options=["Single", "Married"])

    params['employment_type'] = st.selectbox("What employment type do you have?",
                                   options=["Permanent", "Self-employed", "Student/Trainee", "Pension/Retired",
                                            "Temporary", "Other", "Unemployed", "Part-time", "On Leave Income",
                                            "State Income", "Paid by Hour"])

    params['payment_complaints'] = st.selectbox("How many payment complaints do you have?",
                                      options=list(range(1, 11)))

    params['num_dependants'] = st.selectbox("How many kids do you have?",
                                  options=list(range(1, 11)))

    desired_repayment_years = st.selectbox("What is your desired repayment time in years for this loan?",
                                           options=list(range(1, 19)))

    params['desired_repayment_months'] = desired_repayment_years * 12

    params['living_arrangement'] = st.selectbox("Do you rent or own your current home?",
                                      options=["Owned", "Rented"])


    submit_button = st.button("Submit")

    if submit_button:
        ## not working, need to be implemented
        ## load the pipeline from a pickle file
        # model = load_model()

        # create a dataframe from the form data
        X = pd.DataFrame(params, index=[0])
        # make a prediction
        #y_pred = model.predict(X)

        #st.write(f"Your loan application is {y_pred[0]}")

        # Process the form data and perform further actions (e.g., model prediction)
        # You can access the entered values using the variables above
        # For example, `total_loan`, `new_loan`, `monthly_income`, etc.
        pass

loan_application_form()
