import pandas as pd # Load CSV file
csv_data = pd.read_csv('train.csv')
# Display the first few rows of the CSV file 
print("First few rows of CSV file:") 
print(csv_data.head())
# Summary statistics
print("\nSummary statistics of CSV file:") 
print(csv_data.describe())
# Information about columns
print("\nInformation about columns in CSV file:") 
print(csv_data.info())
