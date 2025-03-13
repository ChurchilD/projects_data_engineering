import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sales data (assuming a CSV file)
data = pd.read_csv('AusApparalSales4thQrt2020.csv')

# Display the first few rows of the data to understand its structure
data.head()

# Check for missing values
data.isnull().sum()

# Fill or drop missing values based on the analysis needs
data.dropna(subset=['Sales', 'State'], inplace=True)

# Convert 'date' column to datetime if it's not already
data['Date'] = pd.to_datetime(data['Date'])

# Check for duplicates and remove them if necessary
data = data.drop_duplicates()

# Display cleaned data
data.head()

# Group data by 'state' and sum the 'Sales' for each state
state_Sales = data.groupby('State')['Sales'].sum().reset_index()

# Sort states by total Sales in descending order
state_Sales = state_Sales.sort_values(by='Sales', ascending=False)

# Display the states with the highest Sales
print(state_Sales)

# Calculate the average Sales across all states
average_Sales = state_Sales['Sales'].mean()

# Find states where Sales is below average
low_Sales_states = state_Sales[state_Sales['Sales'] < average_Sales]

# Display the low-Sales states
print("States with below average Sales:")
print(low_Sales_states)

low_Sales_data = data[data['State'].isin(low_Sales_states['State'])]
category_Sales = low_Sales_data.groupby('Group')['Sales'].sum().reset_index()

# Sort categories by Sales
category_Sales = category_Sales.sort_values(by='Sales', ascending=False)
print(category_Sales)


# Group by store location within low-Sales states
store_location_Sales = low_Sales_data.groupby('State')['Sales'].sum().reset_index()

# Sort store locations by Sales
store_location_Sales = store_location_Sales.sort_values(by='Sales', ascending=False)
print(store_location_Sales)

# Plot total Sales by state
plt.figure(figsize=(12,6))
sns.barplot(x='State', y='Sales', data=state_Sales)
plt.xticks(rotation=90)
plt.title('Sales by State (Fourth Quarter)')
plt.xlabel('State')
plt.ylabel('Total Sales ($)')
plt.show()

# Visualizing states with below average Sales
plt.figure(figsize=(12,6))
sns.barplot(x='State', y='Sales', data=low_Sales_states)
plt.xticks(rotation=90)
plt.title('States with Below Average Sales')
plt.xlabel('State')
plt.ylabel('Sales ($)')
plt.show()

