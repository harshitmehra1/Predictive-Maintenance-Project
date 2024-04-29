
#!/bin/bash

echo 'Starting the project automation script...'

# Ensure the script runs from the root directory of the project
cd "$(dirname "$0")"

echo "Running from directory: $(pwd)"

# Data Cleaning
echo 'Running data cleaning script...'
python3 scripts/data_cleaning.py

# Data Enhancing
echo 'Running data enhancing script...'
python3 scripts/data_enhancing.py

# Data Exploration
echo 'Running data exploration script...'
python3 scripts/data_exploration.py

# Model Training
echo 'Running model training script...'
python3 scripts/model_training.py

echo 'All processes completed successfully!'
