import pandas as pd

# Read the CSV file
data = pd.read_csv('data/Levels_Fyi_Salary_Data.csv')

# Create a dataset from the CSV data
dataset = pd.DataFrame(data)


# Get the column names as an array
column_names = dataset.columns.tolist()

# Print the column names
print(column_names)

#print(dataset)
