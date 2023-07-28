import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1', low_memory=False)

# Display the first few rows of the dataset
print(data.head())

# Check the dimensions of the dataset
print(f"Dataset shape: {data.shape}")

# Check the columns in the dataset
print(f"Columns: {data.columns}")

# Check the data types of the columns
print(data.dtypes)

# Check for missing values
print(f"Missing values:\n{data.isnull().sum()}")

# Perform summary statistics
print(data.describe())

# Plot a bar chart of the number of terrorist attacks by year
plt.figure(figsize=(12, 6))
attacks_by_year = data.groupby('iyear').size().reset_index(name='count')
sns.barplot(x='iyear', y='count', data=attacks_by_year)
plt.title('Number of Terrorist Attacks by Year')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=90)
plt.show()

# Plot a pie chart of the attack types
plt.figure(figsize=(10, 10))
attack_types = data['attacktype1_txt'].value_counts()
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)[:len(attack_types)]
plt.pie(attack_types, labels=attack_types.index, explode=explode, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Attack Types')
plt.axis('equal')
plt.show()

# Plot a countplot of the terrorist groups with the most attacks
plt.figure(figsize=(12, 6))
terrorist_groups = data['gname'].value_counts()[:10]
sns.countplot(y='gname', data=data, order=terrorist_groups.index)
plt.title('Top 10 Terrorist Groups with the Most Attacks')
plt.xlabel('Number of Attacks')
plt.ylabel('Terrorist Group')
plt.show()
