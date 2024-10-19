# Read the Parquet file from S3
import pandas as pd

bucket_name = 'intern-project1'
s3_file_path = 'interns/ecommerce_events.parquet'

#df = pd.read_parquet(f's3://{bucket_name}/{s3_file_path}')
df = pd.read_csv("ecommerce_events.csv")
# Display the first few rows to verify the data
# Basic information about the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Check the unique values in event_type to understand the types of events
print(df['event_type'].unique())

# Descriptive statistics for numerical columns
#print(df.describe())
