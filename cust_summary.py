import pandas as pd

# Sample DataFrame: Replace this with your existing DataFrame
# Assuming df is your main DataFrame with event data
file_path = "ecommerce_events.csv"
df = pd.read_csv(file_path)
df['event_time'] = pd.to_datetime(df['event_time'])

# Create a customer summary
customer_summary = df.groupby('user_id').agg(
    purchase=('event_type', lambda x: (x == 'purchase').sum()),  # Count of purchases
    total_spent=('price', 'sum'),  # Total amount spent
    last_purchase_time=('event_time', 'max')  # Most recent purchase
).reset_index()

# Calculate Customer Lifetime Value (CLV)
customer_summary['lifetime_value'] = customer_summary['total_spent']  # For simplicity, you can refine this later

# Save customer_summary DataFrame to a CSV file
customer_summary.to_csv('customer_summary.csv', index=False)
