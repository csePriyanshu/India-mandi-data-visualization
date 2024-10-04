import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create the directory if it doesn't exist
output_dir = 'graphs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('data/mandi_dataset.csv')

columns = df.columns.tolist()
print(columns)

# Step 2: Group by 'State' and count unique 'Market' and unique 'District'
state_summary = df.groupby('State').agg({'Market': 'nunique', 'District': 'nunique'}).reset_index()

# Step 3: Sort the DataFrame by 'State' in alphabetical order
state_summary = state_summary.sort_values('State')

# Step 4: Reverse the order to have states starting from the top
state_summary = state_summary[::-1]

# Step 5: Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plotting number of markets in the first subplot
bars1 = ax1.barh(state_summary['State'], state_summary['Market'], color='lightblue', edgecolor='black')
ax1.set_title('Number of Markets Participating from Each State', fontsize=16, fontweight='bold')
ax1.set_xlabel('Number of Markets', fontsize=14)
ax1.tick_params(axis='y', labelsize=12)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Adding data labels on the bars for markets
for index, value in enumerate(state_summary['Market']):
    ax1.text(value, index, str(value), va='center', fontsize=10)

# Adding legend for markets
ax1.legend([bars1[0]], ['Number of Markets'], loc='upper right', fontsize=12)

# Plotting number of districts in the second subplot
bars2 = ax2.barh(state_summary['State'], state_summary['District'], color='lightgreen', edgecolor='black')
ax2.set_title('Number of Districts Participating from Each State', fontsize=16, fontweight='bold')
ax2.set_xlabel('Number of Districts', fontsize=14)
ax2.tick_params(axis='y', labelsize=12)
ax2.grid(axis='x', linestyle='--', alpha=0.7)

# Adding data labels on the bars for districts
for index, value in enumerate(state_summary['District']):
    ax2.text(value, index, str(value), va='center', fontsize=10)

# Adding legend for districts
ax2.legend([bars2[0]], ['Number of Districts'], loc='upper right', fontsize=12)

# Adjust layout
plt.tight_layout()

# Save the figure before showing it
plt.savefig(f'{output_dir}/statesVSmarket&district.png', bbox_inches='tight')  # Save as PNG

# Show the plot
plt.show()

# Close the figure if you want to free up memory
plt.close()
