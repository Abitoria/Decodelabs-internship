# Exploratory Data Analysis (EDA)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# load the clean data set
df = pd.read_excel("cleaned_Dataset_for_Data_Analytics.xlsx")
# inspect the data

print(df.info())
print(df.shape)

# check for outliers in my data


def find_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"{column}: {len(outliers)} outliers found (bounds: {lower_bound:.2f} to {upper_bound:.2f})")
    return outliers


for col in ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']:
    find_outliers_iqr(df, col)

fig, axes = plt.subplots(1, 4, figsize=(16, 5))
for i, col in enumerate(['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']):
    sns.boxplot(y=df[col], ax=axes[i], color='#5A6E4E')
    axes[i].set_title(col)
plt.tight_layout()
plt.savefig('boxplots.png', dpi=150)
plt.show()

# Numeric and Categorical summary
print(df.describe())
print(df.describe(include='object'))

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.histplot(df['Quantity'], bins=5, ax=axes[0, 0], color='#5A6E4E')
axes[0, 0].set_title('Quantity Distribution')

sns.histplot(df['UnitPrice'], bins=20, ax=axes[0, 1], color='#5A6E4E')
axes[0, 1].set_title('Unit Price Distribution')

sns.histplot(df['TotalPrice'], bins=20, ax=axes[1, 0], color='#5A6E4E')
axes[1, 0].set_title('Total Price Distribution')

sns.histplot(df['ItemsInCart'], bins=10, ax=axes[1, 1], color='#5A6E4E')
axes[1, 1].set_title('Items In Cart Distribution')

plt.tight_layout()
plt.savefig('numeric_distributions.png', dpi=150)
plt.show()


fig, axes = plt.subplots(2, 2, figsize=(14, 10))

df['Product'].value_counts().plot(kind='bar', ax=axes[0, 0], color='#5A6E4E')
axes[0, 0].set_title('Orders by Product')
axes[0, 0].tick_params(axis='x', rotation=45)

df['PaymentMethod'].value_counts().plot(
    kind='bar', ax=axes[0, 1], color='#5A6E4E')
axes[0, 1].set_title('Orders by Payment Method')
axes[0, 1].tick_params(axis='x', rotation=45)

df['OrderStatus'].value_counts().plot(
    kind='bar', ax=axes[1, 0], color='#5A6E4E')
axes[1, 0].set_title('Orders by Status')
axes[1, 0].tick_params(axis='x', rotation=45)

df['ReferralSource'].value_counts().plot(
    kind='bar', ax=axes[1, 1], color='#5A6E4E')
axes[1, 1].set_title('Orders by Referral Source')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('categorical_breakdowns.png', dpi=150)
plt.show()

# Monthly revenue trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()

plt.figure(figsize=(14, 5))
monthly_sales.plot(kind='line', marker='o', color='#5A6E4E')
plt.title('Total Revenue by Month')
plt.ylabel('Total Revenue ($)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png', dpi=150)
plt.show()

# Correlation
corr = df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']].corr()
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='Greens', fmt='.2f')
plt.title('Correlation Between Numeric Variables')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=150)
plt.show()

# Average order value by product
avg_by_product = df.groupby(
    'Product')['TotalPrice'].mean().sort_values(ascending=False)
print(avg_by_product)
