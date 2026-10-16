import os
import pandas as pd
from sklearn.datasets import fetch_california_housing

# 1. Load the dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# 2. Define your desired folder path
# Replace this with your actual folder path (e.g., "C:/Users/Name/Documents/" on Windows)
target_path = "./data/" 

# 3. Create the directory if it doesn't exist
os.makedirs(target_path, exist_ok=True)

# 4. Save to the specific path
full_file_path = os.path.join(target_path, "california_housing.csv")
df.to_csv(full_file_path, index=False)

print(f"Dataset successfully saved to: {full_file_path}")
