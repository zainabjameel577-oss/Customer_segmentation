import pandas as pd 
import matplotlib.pyplot as plt

file_path = "data/online_retail_II.xlsx"
df = pd.read_excel(file_path, sheet_name= 0)

#loading and testing data
# print("First 5 rows:")
# print(df.head())
# print("\nDataset shape:")
# print(df.shape)
# print("\nColumn names:")
# print(df.columns)

#checking missing values in colums and summing it
# print("\nMissing values in each column:")
# print(df.isnull().sum())

# #chek missing customers
# missing_customers = df[df["Customer ID"].isnull()]
# print("Rows with missing Customer ID:", len(missing_customers))
# print("\nSample rows with missing Customer ID:")
# print(missing_customers.head())

#cleaning missing values in customer id
df_clean = df.dropna(subset = ['Customer ID']).copy()
print("\nMissing Customer IDs after cleaning:")
print(df_clean["Customer ID"].isnull().sum())

#checking cancelled invoices
# cancelled = df_clean[df_clean['Invoice'].astype('str').str.startswith("C")]

# #check negative quantities 
# neg_quantities = df_clean[df_clean['Quantity'] < 0]
# print("\nRows with negative quantities:", len(neg_quantities))

#  #check invalid pricing
# invalid_prices = df_clean[df_clean["Price"] <= 0]
# print("\nRows with zero or negative prices:", len(invalid_prices))

# print(invalid_prices.head())
# print(neg_quantities.head())

df_cluster = df_clean.copy()

df_cluster = df_cluster[
    (~df_cluster["Invoice"].str.startswith("C", na=False)) &
    (df_cluster["Quantity"] > 0) &
    (df_cluster["Price"] > 0)
].copy()

duplicate = df_cluster[df_cluster.duplicated(keep=False)]
print(duplicate.head(10))
print("Rows involved in duplicates:", len(duplicate))
print("rows to be deleted:", df_cluster.duplicated().sum())

#removing the duplicate items excluding first occurence
df_cluster = df_cluster.drop_duplicates().copy()

print("\nRows remaining:", len(df_cluster))
print("\nDuplicates remaining:", df_cluster.duplicated().sum())

#narrowing down the rows
df_cluster["TotalAmount"] = df_cluster["Quantity"] * df_cluster["Price"]
print(df_cluster.head())

customer_data = df_cluster.groupby("Customer ID").agg(
    TotalSpent=("TotalAmount", "sum"),
    TotalQuantity=("Quantity", "sum"),
    InvoiceCount=("Invoice", "nunique")
).reset_index()

customer_data.head()

customer_data.to_csv("customer_data.csv", index=False)

print(customer_data.shape)
print(customer_data.isnull().sum())
print(customer_data.describe())

#visualizing
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.boxplot(customer_data["TotalSpent"])
plt.title("Total Spending")

plt.subplot(1, 3, 2)
plt.boxplot(customer_data["TotalQuantity"])
plt.title("Total Quantity")

plt.subplot(1, 3, 3)
plt.boxplot(customer_data["InvoiceCount"])
plt.title("Invoice Count")

plt.tight_layout()
plt.show()

print(customer_data[["TotalSpent", "TotalQuantity", "InvoiceCount"]].describe())