import pandas as pd

# Load cleaned dataset
df = pd.read_excel("cleaned_data.xlsx")

# Optional safety (good practice)
df.columns = df.columns.str.strip()

#Total Profit by country
profit_country = df.groupby("Country")["Profit"].sum().sort_values(ascending=False)
print("\nTotal Profit by Country:\n", profit_country)




#Total Sales by Year
sales_year = df.groupby("Year")["Sales"].sum()
print(sales_year)


#Profit by Segment
profit_segment = df.groupby("Segment")["Profit"].sum()
print(profit_segment)



#Monthly Sales Trend
monthly_sales = df.groupby("Month Name")["Sales"].sum()
print(monthly_sales)
