import pandas as pd;
import clean_dataset as dataset;
import matplotlib.pyplot as plt

dataset_tot=dataset.dataset;

#cost of living in New York city in dollar, 1 bedroom apartament outside city center numbeo

cost_newyork=4000;
print(dataset_tot.columns)

dataset_tot["Savings"]=dataset_tot['net_salary'] -cost_newyork*12/100*dataset_tot['Cost of Living Plus Rent Index'];

# Sort the dataset by savings in descending order
dataset_tot= dataset_tot.sort_values('Savings', ascending=True)

# Create the horizontal bar chart
plt.barh(dataset_tot['City'], dataset_tot['Savings'], color='steelblue')

# Add labels and title
plt.xlabel('Savings')
plt.ylabel('City')
plt.title('Savings by City')

# Add grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Customize tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Adjust spacing
plt.tight_layout()

# Display the plot
plt.show()


