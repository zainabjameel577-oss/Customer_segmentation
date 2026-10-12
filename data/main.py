import pandas as pd 
file_path = "data/online_retail_II.xlsx"
df = pd.read_excel(file_path, sheet_name= 0)

#loading and testing data
print("First 5 rows:")
print(df.head())
print("\nDataset shape:")
print(df.shape)
print("\nColumn names:")
print(df.columns)

#checking missing values in colums and summing it
print("\nMissing values in each column:")
print(df.isnull().sum())


missing_customers = df[df["Customer ID"].isnull()]

print("Rows with missing Customer ID:", len(missing_customers))

print("\nSample rows with missing Customer ID:")
print(missing_customers.head())

#cleaning missing values in customer id
df_clean = df.dropna(subset = ['Customer ID']).copy()
print("\nMissing Customer IDs after cleaning:")
print(df_clean["Customer ID"].isnull().sum())

#checking cancelled invoices
cancelled = df_clean['Invoice'].astype('str').