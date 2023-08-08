import pandas as pd

# Read data from CSV file
input_file = 'input_data.csv'
output_file = 'output_data.csv'

# Load CSV data into a DataFrame
data = pd.read_csv(input_file)

# Perform data processing (adding 5 years to Age)
data['Age'] = data['Age'] + 10

# Save processed data to a new CSV file
data.to_csv(output_file, index=False)

print("Data automation complete. Processed data saved to", output_file)
