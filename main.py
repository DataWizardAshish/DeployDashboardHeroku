# Check the original DataFrame for purchase events
import pandas as pd

# bucket_name = 'intern-project1'
# s3_file_path = 'interns/ecommerce_events.parquet'

df = pd.read_csv("ecommerce_events.csv")
purchase_events = df[df['event_type'] == 'purchase']
print(purchase_events.head())  # Display the first few rows of purchase events
print(purchase_events['user_id'].value_counts())  # Count purchases per user
