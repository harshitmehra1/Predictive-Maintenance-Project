# Data visualization and analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set the base directory to the directory of this script
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the path for the cleaned data file
data_path = os.path.join(base_dir, 'data', 'CleanedData.csv')
print("Loading data from:", data_path)

# Load the data
data = pd.read_csv(data_path)

# Select numeric data types for analysis
data_numeric = data.select_dtypes(include=[np.number])

# Print general statistics
print("General Statistics:")
print(data_numeric.describe())

# Print and visualize the correlation matrix
print("\nCorrelation Matrix:")
correlation_matrix = data_numeric.corr()
print(correlation_matrix)

# Heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",  # two decimal places
    cmap='coolwarm'  # color map for highlighting
)
plt.title('Correlation Matrix')
plt.show()

# Histograms for non-binary numeric features
non_binary_columns = [
    col for col in data_numeric.columns if not all(data[col].isin([0, 1]))
]
data[non_binary_columns].hist(
    bins=15,  # number of bins
    figsize=(15, 10),  # size of the figures
    layout=(3, 3)  # layout for subplots
)
plt.suptitle('Feature Distributions')
plt.show()
