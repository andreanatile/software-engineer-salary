import pandas as pd
import clean_dataset as dataset
import matplotlib.pyplot as plt
import numpy as np

dataset_tot = dataset.dataset

# cost of living in New York city in dollar, 1 bedroom apartament outside city center numbeo
cost_newyork = 4000

# ------------------------------- create new columns ------------------------------

# calculate yearly cost of living per city
dataset_tot['cost_living_per_year'] = cost_newyork * \
    dataset_tot['Cost of Living Plus Rent Index']*12/100

# calculate savings per city
dataset_tot["Savings"] = dataset_tot['net_salary'] - \
    dataset_tot['cost_living_per_year']

# calculate taxes
dataset_tot['Taxes'] = dataset_tot['gross_salary']-dataset_tot['net_salary']

# -------------------------------- plot ---------------------------------------------

# Sort the dataset by savings in descending order
dataset_tot = dataset_tot.sort_values('Savings', ascending=True)

# Create a figure and axis
fig, ax = plt.subplots()

# Calculate the positions of the bars on the x-axis
x = range(len(dataset_tot))

# Define new colors for the bars
savings_color = '#6A0572'
taxes_color = '#DC143C'
cost_color = '#228B22'

# Plotting the stacked bars
ax.bar(x, dataset_tot['Savings'], color=savings_color, label='Savings')
ax.bar(x, dataset_tot['Taxes'], color=taxes_color,
       label='Taxes', bottom=dataset_tot['Savings'])
ax.bar(x, dataset_tot['cost_living_per_year'], color=cost_color, label='Cost of living per year',
       bottom=dataset_tot['Savings'] + dataset_tot['Taxes'])

# Set the x-axis tick positions and labels
ax.set_xticks(x)
ax.set_xticklabels(dataset_tot['City'], rotation=45, ha='right')

# Set the y-axis label in dollars
ax.set_ylabel('Amount ($)', fontsize=12)

# Format the y-axis labels with a decimal point at the thousands position
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: format(x, ',.0f')))


# Set the chart title
ax.set_title(
    'Gross Income and Savings Comparison for Software Engineers in Top Paying Cities')

# Remove the background
ax.set_facecolor('none')
fig.set_facecolor('white')

# Add a legend
ax.legend()

# Remove the border around the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Adjust the layout to prevent label cropping
plt.tight_layout()

# Show the plot
plt.show()
