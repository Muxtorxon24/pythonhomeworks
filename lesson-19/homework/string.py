import pandas as pd

# Ma'lumotlarni yuklash
df = pd.read_csv(r'lesson-10/homework/task/sales_data.csv')

# 1. Kategoriyalar bo‘yicha umumiy statistika
category_stats = df.groupby('Category').agg(
    total_quantity=('Quantity', 'sum'),
    avg_price=('Price', 'mean'),
    max_quantity=('Quantity', 'max')
)
print("Category Statistics:\n", category_stats)

# 2. Har bir kategoriya bo‘yicha eng ko‘p sotilgan mahsulot
top_products = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.loc[top_products.groupby('Category')['Quantity'].idxmax()]
print("Top-selling Products:\n", top_products)

# 3. Eng ko‘p savdo bo‘lgan sana
df['Total_Sales'] = df['Quantity'] * df['Price']
top_sales_date = df.groupby('Date')['Total_Sales'].sum().idxmax()
print("Date with Highest Total Sales:", top_sales_date)



# Ma'lumotlarni yuklash
df = pd.read_csv(r'task\customer_orders.csv')

# 1. 20 tadan kam buyurtma qilgan mijozlarni chiqarib tashlash
customer_orders = df.groupby('CustomerID')['OrderID'].count()
filtered_customers = customer_orders[customer_orders >= 20].index
df_filtered = df[df['CustomerID'].isin(filtered_customers)]
print("Filtered Customers:\n", df_filtered)

# 2. O'rtacha mahsulot narxi $120 dan katta bo‘lgan mijozlar
avg_price_per_customer = df.groupby('CustomerID')['Price'].mean()
high_value_customers = avg_price_per_customer[avg_price_per_customer > 120].index
print("High-value Customers:\n", high_value_customers)

# 3. Har bir mahsulot uchun umumiy miqdor va narx hisoblash, 5 tadan kam sotilganlarni chiqarib tashlash
product_stats = df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
)
filtered_products = product_stats[product_stats['total_quantity'] >= 5]
print("Filtered Products:\n", filtered_products)




import sqlite3
import pandas as pd

# **1. Ma'lumotlarni SQLite dan yuklash**
conn = sqlite3.connect(r'task\population.db')
query = "SELECT * FROM population"
df = pd.read_sql(query, conn)
conn.close()

# **2. Salary band ma'lumotlarini yuklash**
salary_bands = pd.read_excel(r'task\population salary analysis.xlsx')

# **3. Salary band bo‘yicha statistikalar**
df['Salary_Band'] = pd.cut(df['Salary'], bins=salary_bands['Bins'], labels=salary_bands['Categories'])

salary_stats = df.groupby('Salary_Band').agg(
    percentage_population=('Salary', lambda x: len(x) / len(df) * 100),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    total_population=('Salary', 'count')
)
print("Salary Statistics:\n", salary_stats)

# **4. Har bir shtat bo‘yicha shu statistika**
state_salary_stats = df.groupby(['State', 'Salary_Band']).agg(
    percentage_population=('Salary', lambda x: len(x) / len(df) * 100),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    total_population=('Salary', 'count')
)
print("State-wise Salary Statistics:\n", state_salary_sta
