import streamlit as st
import pandas as pd

# Load the customer summary data
customer_summary = pd.read_csv('customer_summary.csv')
customer_summary = customer_summary[customer_summary['purchase'] > 0]
# Set the title of the app
st.title("Customer Summary Dashboard")

# Display the customer summary as a table
st.subheader("Customer Summary Table")
st.dataframe(customer_summary)

# Visualize the total spending by user
st.subheader("Total Spending by User")
st.bar_chart(customer_summary.set_index('user_id')['total_spent'])

# Visualize the number of purchases by user
st.subheader("Number of Purchases by User")
st.bar_chart(customer_summary.set_index('user_id')['purchase'])

# Visualize customer lifetime value
st.subheader("Customer Lifetime Value")
st.bar_chart(customer_summary.set_index('user_id')['lifetime_value'])
