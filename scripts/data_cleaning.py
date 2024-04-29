
# Data Cleaning

import pandas as pd
import os

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Path to the input data
data_path = os.path.join(dir_path, '../data/NotCleanedData.csv')
print("Attempting to open data file at path:", data_path)

# Now read the file
data = pd.read_csv(data_path)
print(data.head())

# Remove unnecessary columns
data_cleaned = data.drop(['UDI', 'Product ID'], axis=1)

# Checking for any missing values
missing_values = data_cleaned.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Saved the cleaned data to a new CSV file
cleaned_data_path = os.path.join(dir_path, '../data/CleanedData.csv')
data_cleaned.to_csv(cleaned_data_path, index=False)

print("Data cleaning complete. Cleaned data saved to:", cleaned_data_path)
