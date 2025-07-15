import pandas as pd # Load Excel file
excel_data = pd.read_excel('Sample - Superstore.xlsx', sheet_name='Orders') # Display the first few rows of the Excel file
print("First few rows of Excel file:") 
print(excel_data.head())
# Summary statistics
print("\nSummary statistics of Excel file:") 
print(excel_data.describe())
# Information about columns
print("\nInformation about columns in Excel file:") 
print(excel_data.info())
