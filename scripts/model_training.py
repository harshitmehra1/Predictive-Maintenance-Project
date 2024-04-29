# Training our Model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

import os

# Path for the enhanced data file :
data_path = 'data/EnhancedData.csv'             # Relative path from the project root
full_data_path = os.path.abspath(data_path)     # Converts to absolute path
print("Loading enhanced data from:", full_data_path)


# Load the enhanced data
data = pd.read_csv(full_data_path)


# Identify and one-hot encode categorical variables
categorical_columns = [column_name for column_name in data.columns if data[column_name].dtype == 'object']
data = pd.get_dummies(data, columns=categorical_columns)

# Define the target and feature set
X = data.drop('Machine failure', axis=1)  # Features
y = data['Machine failure']               # Target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model to disk
model_path = 'model/machine_failure_predictor.pkl'  # Correct relative path for consistency
full_model_path = os.path.abspath(model_path)  # Convert to absolute path
joblib.dump(model, full_model_path)
print(f"Model saved to {full_model_path}")
