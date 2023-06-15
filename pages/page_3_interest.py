import streamlit as st
st.set_page_config(
    page_title="Sambla Group",
    page_icon="",
    layout="wide"
)



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
            text-align: right;
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

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Loan Calculator</h1>", unsafe_allow_html=True)

col1, col_, col2 = st.columns([1, 0.2, 1])
# Page title and layout


# Input sliders
with col1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    loan_amount = st.number_input("Loan Amount", value = 60000)
    repayment_years = st.slider("Repayment Years", 1, 18, 5)
    interest_rate = st.slider("Interest Rate (%)", 1.0, 20.0, 5.0, step=0.1)


# Calculate monthly interest rate and repayment periods
monthly_interest_rate = interest_rate / 100 / 12
repayment_periods = repayment_years * 12

# Calculate monthly payment
monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -repayment_periods)

# Calculate total cost of the loan
total_cost = monthly_payment * repayment_periods

# Calculate separate amortization and interest costs
amortization_cost = loan_amount
interest_cost = (total_cost / repayment_periods) * (interest_rate/100)

with col_:
    st.write("")
with col2:
# Display results
    st.subheader("Loan Details")
    st.markdown("<div><strong>Loan Amount:</strong> €{:,}</div>".format(loan_amount), unsafe_allow_html=True)
    st.markdown("<div><strong>Repayment Years:</strong> {}</div>".format(repayment_years), unsafe_allow_html=True)
    st.markdown("<div><strong>Interest Rate:</strong> {}%</div>".format(interest_rate), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Monthly Payment")
    st.write("€{:.2f}".format(monthly_payment))
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Total Cost")
    st.markdown("<div><strong>Total Cost at the end of {} years:</strong> €{:,.2f}</div>".format(repayment_years, total_cost), unsafe_allow_html=True)
