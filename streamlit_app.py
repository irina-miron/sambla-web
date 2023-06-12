import streamlit as st


def loan_application_form():
    st.title('Loan Application Form')

    total_loan = st.number_input("How much do you want to loan?", step=0.01, value=0.0)
    new_loan = st.number_input("How much of this is new loan on top of what you already have?", step=0.01, value=0.0)
    monthly_income = st.slider("What is your monthly income before tax?", min_value=0, max_value=1231212)

    application_type = st.selectbox("What type of loan is this?",
                                    options=["No Refinance", "Partial Refinance", "Full Refinance"])

    purpose_text = st.selectbox("What are you using the loan for?",
                                options=["Investment", "Other", "Refinance", "Studies", "Vehicle",
                                         "Renovation", "House", "Consume", "Health", "Vacation", "Services"])

    is_first_application = st.checkbox("Is this your first application?")
    is_last_application = st.checkbox("Is this your last application?")

    age = st.number_input("How old are you?", value=0)

    civil_status = st.selectbox("Are you married?", options=["Single", "Married"])

    employment_type = st.selectbox("What employment type do you have?",
                                   options=["Permanent", "Self-employed", "Student/Trainee", "Pension/Retired",
                                            "Temporary", "Other", "Unemployed", "Part-time", "On Leave Income",
                                            "State Income", "Paid by Hour"])

    payment_complaints = st.selectbox("How many payment complaints do you have?",
                                      options=list(range(1, 11)))

    num_dependants = st.selectbox("How many kids do you have?",
                                  options=list(range(1, 11)))

    desired_repayment_years = st.selectbox("What is your desired repayment time in years for this loan?",
                                           options=list(range(1, 19)))

    desired_repayment_months = desired_repayment_years * 12

    living_arrangement = st.selectbox("Do you rent or own your current home?",
                                      options=["Owned", "Rented"])

    submit_button = st.button("Submit")

    if submit_button:
        # Process the form data and perform further actions (e.g., model prediction)
        # You can access the entered values using the variables above
        # For example, `total_loan`, `new_loan`, `monthly_income`, etc.
        pass

loan_application_form()
