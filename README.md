# Predictive Maintenance Project

## Overview
This project implements a predictive maintenance system using machine learning to predict machine failures before they occur. The system uses historical machine data to train a model that can forecast potential breakdowns, enhancing maintenance strategies and reducing operational costs.


## Repository Structure

### `/data`
Contains all the datasets used in the project:
- `CleanedData.csv` - The dataset after initial cleaning to remove irrelevant data and handle missing values.
- `EnhancedData.csv` - The dataset after feature engineering steps such as normalization and log transformations.
- `NotCleanedData.csv` - The original raw dataset.


### `/scripts`
Python scripts used for data processing, analysis, and model training:
- `data_cleaning.py` - Cleans the raw data by handling missing values and removing unnecessary information.
- `data_enhancing.py` - Enhances the data by applying scaling and transformations to improve model accuracy.
- `data_exploration.py` - Contains exploratory data analysis including statistical summaries and visualization of data distributions and correlations.
- `model_training.py` - Trains a predictive model using Random Forest to predict machine failures and evaluates its performance.


### `/model`
- `machine_failure_predictor.pkl` - The trained machine learning model saved for later use or deployment.

### `run_project.sh`
A shell script to automate the entire data processing and model training pipeline:
1. Cleans the data.
2. Enhances the data.
3. Performs exploratory data analysis.
4. Trains the predictive model.
To execute, run:
```bash :  ./run_project.sh                                                               `

## Installation
To run this project, ensure you have Python installed along with the following packages: pandas, numpy, scikit-learn, matplotlib, seaborn, and joblib.


1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages:

Paste this in Bash : { pip install pandas numpy scikit-learn matplotlib seaborn joblib }


.
.
.



## Usage if `run_project.sh` doesn't work.
Run the scripts in the following order to process data, train the model, and perform exploratory analysis:
1. `python3 scripts/data_cleaning.py`
2. `python3 scripts/data_enhancing.py`
3. `python3 scripts/data_exploration.py`
4. `python3 scripts/model_training.py`


