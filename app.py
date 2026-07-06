import streamlit as st
import joblib
import pandas as pd
st.set_page_config(
    page_title="AI Finance Advisor",
    page_icon="💰",
    layout="wide"
)
model = joblib.load("model.pkl")
st.sidebar.title("AI Finance Advisor")

st.sidebar.write("### Features")

st.sidebar.write("✔ Income Analysis")

st.sidebar.write("✔ Expense Analysis")

st.sidebar.write("✔ Savings Prediction")

st.sidebar.write("✔ Financial Advice")

st.sidebar.write("✔ Investment Suggestions")
st.title("AI Powered Personal Finance Advisor")
monthly_income = st.number_input("Enter Monthly Income", min_value=0.0)

monthly_expense_total = st.number_input("Enter Monthly Expense", min_value=0.0)

credit_score = st.number_input("Enter Credit Score", min_value=0)

loan_payment = st.number_input("Enter Loan Payment", min_value=0.0)

investment_amount = st.number_input("Enter Investment Amount", min_value=0.0)

actual_savings = st.number_input("Enter Actual Savings", min_value=0.0)
st.subheader("Financial Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Monthly Income", f"₹{monthly_income:,.0f}")

col2.metric("Monthly Expense", f"₹{monthly_expense_total:,.0f}")

col3.metric("Savings", f"₹{actual_savings:,.0f}")
if st.button("Predict"):
        input_data = pd.DataFrame({
        "monthly_income": [monthly_income],
        "monthly_expense_total": [monthly_expense_total],
        "credit_score": [credit_score],
        "loan_payment": [loan_payment],
        "investment_amount": [investment_amount],
        "actual_savings": [actual_savings]
    })
prediction = model.predict(input_data)
st.success(f"Prediction: {prediction[0]}")
prediction = model.predict(input_data)

if prediction[0] == True:
    st.success("🎉 Congratulations! You are likely to achieve your savings goal.")
else:
    st.error("⚠️ You are not likely to achieve your savings goal.")
    st.subheader("Personalized Financial Advice")
    if monthly_expense_total > monthly_income:
     st.warning("Your expenses are higher than your income. Try reducing unnecessary spending.")
    if actual_savings < 5000:
     st.info("Try to save at least ₹5,000 every month.")
     if investment_amount < 1000:
      st.info("Consider investing a small amount regularly to grow your wealth.")
if credit_score < 650:
    st.warning("Your credit score is low. Pay bills on time and reduce outstanding debt.")
    if actual_savings >= 5000 and monthly_expense_total <= monthly_income:
     st.success("Excellent! You are managing your finances well. Keep it up!")
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
if actual_savings >= 5000 and monthly_expense_total <= monthly_income:
    st.success("Excellent! You are managing your finances well. Keep it up!")
    st.subheader("Financial Summary Chart")
    labels = ["Income", "Expense", "Savings", "Investment"]

values = [
    monthly_income,
    monthly_expense_total,
    actual_savings,
    investment_amount
]
fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_title("Personal Finance Overview")
ax.set_ylabel("Amount")
st.pyplot(fig)
st.success("Thank you for using the AI Powered Personal Finance Advisor!")
st.markdown("---")
st.write("Developed by: Prateeksha Upadhya")