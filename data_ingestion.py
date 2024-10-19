import pandas as pd
import boto3

# Load the dataset locally
file_path = "ecommerce_events.csv"
df = pd.read_csv(file_path)

# Save the dataset as Parquet to S3
bucket_name = 'intern-project1'
s3_file_path = 'interns/ecommerce_events.parquet'

# Save the DataFrame as Parquet format and upload to S3
df.to_parquet(f's3://{bucket_name}/{s3_file_path}', index=False)

print(f"Dataset saved to s3://{bucket_name}/{s3_file_path}")
