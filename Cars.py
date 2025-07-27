import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Cars_dataset.csv")  # Replace with your actual file path

# Initial data overview
print("Initial Shape:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# Handling Missing Values
df['Fuel Type'] = df['Fuel Type'].fillna("Unknown")
df['Transmission'] = df['Transmission'].fillna("Unknown")
df['Owner'] = df['Owner'].fillna("Unknown")

# Fixing Data Types
df['Year'] = df['Year'].astype(int)
df['Price'] = df['Price'].astype(int)
df['Kilometers'] = df['Kilometers'].astype(int)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Data Visualization
# 1. Distribution of Fuel Types
sns.countplot(data=df, x='Fuel Type', order=df['Fuel Type'].value_counts().index)
plt.title("Distribution of Fuel Types")
plt.xticks(rotation=45)
plt.show()

# 2. Transmission Type Count
sns.countplot(data=df, x='Transmission', order=df['Transmission'].value_counts().index)
plt.title("Transmission Type Distribution")
plt.show()

# 3. Transmission Type Percentage
transmission_counts = df['Transmission'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(transmission_counts, labels=transmission_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title("Transmission Type Distribution")
plt.axis('equal')
plt.show()

# 4. Average Price by Brand
avg_price = df.groupby('Brand')['Price'].mean().sort_values(ascending=False).head(10)
avg_price.plot(kind='bar', color='skyblue')
plt.title("Top 10 Brands by Average Price")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.show()

# 5. State-wise Car Count
top_states = df['State'].value_counts().head(10)
top_states.plot(kind='bar', color='orange')
plt.title("Top 10 States by Number of Listings")
plt.ylabel("Number of Cars")
plt.xticks(rotation=45)
plt.show()

# 6. Year-wise Car Listings
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Year', order=sorted(df['Year'].unique()))
plt.title("Number of Cars by Year")
plt.xlabel("Manufacturing Year")
plt.ylabel("Number of Listings")
plt.xticks(rotation=45)
plt.show()

# 7. Average Price by Fuel Type
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Fuel Type', y='Price', estimator='mean', ci=None, palette='pastel')
plt.title("Average Price by Fuel Type")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.show()

# 8. Correlation Heatmap (Numerical Columns Only)
plt.figure(figsize=(10, 6))
numeric_cols = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap (Numerical Features)")
plt.show()

# 9. Pie Chart: Distribution of Owner Types
owner_counts = df['Owner'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(owner_counts, labels=owner_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title("Owner Type Distribution")
plt.axis('equal')
plt.show()

# 10. Pie Chart: Fuel Type Distribution
accident_counts = df['Accidental'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(accident_counts, labels=accident_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title("Accidental Cars Distribution")
plt.axis('equal')
plt.show()


