# data cleaning with decode lab
import pandas as pd  

df = pd.read_excel(
    r"C:\Users\Administrator\Desktop\copy_Dataset for Data Analytics.xlsx")

print(df.head())  

# inspect the data
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())      

# check the column with the empty data set
print(df['CouponCode'].unique())
print(df['CouponCode'].isna().sum())
print(df['CouponCode'].apply(lambda x: repr(x)).value_counts())

# See rows where coupon code is missing
print(df[df['CouponCode'].isna()])
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')


print(df['CouponCode'].isna().sum())  
print(df['CouponCode'].value_counts())

# Count how many rows have a coupon code vs not
# Strip whitespace from all text columns
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].str.strip()
print("Duplicate OrderIDs:", df['OrderID'].duplicated().sum())
print("Invalid dates:", df['Date'].isna().sum())

print("Duplicate rows after cleaning:", df.duplicated().sum())
print("Duplicate OrderIDs after cleaning:", df['OrderID'].duplicated().sum())

#  saved clean data set
df.to_excel("cleaned_Dataset_for_Data_Analytics.xlsx", index=False)
print("Cleaned file saved!")
