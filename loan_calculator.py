import streamlit as st

def loan_calculator():
    st.title("Private Loan Calculator")

    # Input sliders
    loan_amount = st.slider("Loan Amount (€)", 1, 5000)
    repayment_years = st.slider("Repayment Years", 1, 18)
    interest_rate = st.slider("Interest Rate (%)", 1.0, 20.0, step=0.1)

    # Calculate monthly interest rate and repayment periods
    monthly_interest_rate = interest_rate / 100 / 12
    repayment_periods = repayment_years * 12

    # Calculate monthly payment
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -repayment_periods)

    # Calculate total cost of the loan
    total_cost = monthly_payment * repayment_periods

    # Calculate separate amortization and interest costs
    amortization_cost = loan_amount
    interest_cost = total_cost - loan_amount

    # Display results
    st.subheader("Loan Details")
    st.write(f"Loan Amount: €{loan_amount}")
    st.write(f"Repayment Years: {repayment_years}")
    st.write(f"Interest Rate: {interest_rate}%")

    st.subheader("Monthly Payment")
    st.write(f"€{monthly_payment:.2f}")

    st.subheader("Cost Breakdown")
    st.write(f"Amortization Cost: €{amortization_cost:.2f}")
    st.write(f"Interest Cost: €{interest_cost:.2f}")
    st.write(f"Total Cost at the end of {repayment_years} years: €{total_cost:.2f}")

# Run the loan calculator
loan_calculator()
