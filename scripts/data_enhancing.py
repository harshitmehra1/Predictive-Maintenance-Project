
# Data enhancing and adding features

import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load the cleaned data
data_path = os.path.join(dir_path, '../data/CleanedData.csv')
print("Loading data from:", data_path)
data = pd.read_csv(data_path)

# Log Transformation
# Check if the feature 'Torque [Nm]' is highly skewed and apply log transformation if necessary
if data['Torque [Nm]'].skew() > 0.75:
    data['log_torque'] = np.log(data['Torque [Nm]'] + 1)  # Adding 1 to avoid log(0)
    print("Applied log transformation to 'Torque [Nm]' to reduce skewness.")

# Normalization or Standardization
# Standardizing temperatures to have zero mean and unit variance
scaler = StandardScaler()
data[['Air temperature [K]', 'Process temperature [K]']] = scaler.fit_transform(data[['Air temperature [K]', 'Process temperature [K]']])
print("Standardized temperatures to have zero mean and unit variance.")

# Save the engineered data to a new CSV file
enhanced_data_path = os.path.join(dir_path, '../data/EnhancedData.csv')
data.to_csv(enhanced_data_path, index=False)

print("Data enhancing complete. Enhanced data saved to:", enhanced_data_path)



'''

This file performs key transformations to prepare the dataset for machine learning models.
It includes applying a logarithmic transformation to highly skewed features to normalize their distributions
and standardizing certain features to ensure they contribute equally to model training.
These steps are intended to enhance the data's predictive power, 
enabling models to train more effectively and accurately.

'''
