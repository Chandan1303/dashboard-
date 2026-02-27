import pandas as pd


df = pd.read_excel("Sample data - week4.xlsx")


df.columns = df.columns.str.strip()


print(df.isnull().sum())

df = df.drop_duplicates()

df["Discount Band"] = df["Discount Band"].fillna("No Discount")

df["Date"] = pd.to_datetime(df["Date"])

df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100


df.to_excel("cleaned_data.xlsx", index=False)

print("Cleaning Completed Successfully ")
