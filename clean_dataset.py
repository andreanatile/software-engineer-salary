import pandas as pd

# Read the income CSV file with ";" separator
dataset_income = pd.read_csv('data/income.csv', sep=';')

# Drop the first column
dataset_income = dataset_income.iloc[:, 1:]
dataset_income=dataset_income.drop(columns=['state'])

#Read the Cost of living CSV file
dataset_Cost_Living=pd.read_csv('data/Cost_of_living_index.csv')


# Extract city names without additional information and cleaning 
dataset_Cost_Living=dataset_Cost_Living.drop(columns=['Rank','Restaurant Price Index','Cost of Living Index','Groceries Index'])
dataset_Cost_Living=dataset_Cost_Living[dataset_Cost_Living['City']!='London, Canada']
dataset_Cost_Living=dataset_Cost_Living[dataset_Cost_Living['City']!='Vancouver, WA, United States']
dataset_Cost_Living=dataset_Cost_Living[dataset_Cost_Living['City']!='Portland, ME, United States']
dataset_Cost_Living['City'] = dataset_Cost_Living['City'].str.split(',', n=1).str[0].str.strip()

# Merge datasets based on the 'City' column
dataset= pd.merge(dataset_income, dataset_Cost_Living, on='City', how='inner')

print(dataset['City'])