import streamlit as st
from datetime import date

# Page setup
st.set_page_config(page_title="Age Calculator", page_icon="📅", layout="centered")

# App title
st.title("📅 Age Calculator")
st.write("Enter your date of birth to calculate your exact age.")

# Input date
dob = st.date_input("Select your date of birth:", min_value=date(1900, 1, 1), max_value=date.today())

# Calculate age
if st.button("Calculate Age"):
    today = date.today()
    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    # Adjust if the current month/day hasn't occurred yet this year
    if age_days < 0:
        age_months -= 1
        prev_month = (today.month - 1) if today.month > 1 else 12
        prev_month_year = today.year if today.month > 1 else today.year - 1
        last_day_prev_month = (date(prev_month_year, prev_month + 1, 1) - date(prev_month_year, prev_month, 1)).days
        age_days += last_day_prev_month

    if age_months < 0:
        age_years -= 1
        age_months += 12

    st.success(f"🎉 You are {age_years} years, {age_months} months, and {age_days} days old.")
