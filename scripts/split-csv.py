import pandas as pd
import os

# Path for the input CSV file
input_csv_path = 'C:/Users/yilve/Documents/Personal Projects/wifi-map-tracker-hk/wifi-map-hk.csv'

# Number of items per smaller CSV file
items_per_file = 1500

# Read the input CSV using pandas
df = pd.read_csv(input_csv_path)

# Calculate the number of smaller files needed
num_files = len(df) // items_per_file + (1 if len(df) % items_per_file > 0 else 0)

# Split the DataFrame and save as smaller CSV files
for file_number in range(num_files):
    start_idx = file_number * items_per_file
    end_idx = (file_number + 1) * items_per_file
    smaller_df = df.iloc[start_idx:end_idx]

    output_csv_path = f'smaller_file_{file_number + 1}.csv'
    smaller_df.to_csv(output_csv_path, index=False)

print(f'Split into {num_files} smaller CSV files.')