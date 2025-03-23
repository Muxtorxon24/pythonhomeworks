import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# 1. O'rtacha baho hisoblash
df1["Average"] = df1[['Math', 'English', 'Science']].mean(axis=1)

# 2. Eng yuqori o'rtacha bahoga ega talabani topish
top_student = df1.loc[df1["Average"].idxmax()]

# 3. Umumiy ball (Total) ustuni qo'shish
df1["Total"] = df1[['Math', 'English', 'Science']].sum(axis=1)

# 4. O'rtacha baholarni ustunli diagramma sifatida chiqarish
df1[['Math', 'English', 'Science']].mean().plot(kind='bar', color=['blue', 'red', 'green'])
plt.xlabel("Fanlar")
plt.ylabel("O'rtacha baho")
plt.title("Har bir fan bo‘yicha o'rtacha baho")
plt.show()

print("Eng yaxshi o'rtacha bahoga ega talaba:")
print(top_student)



data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# 1. Har bir mahsulot bo'yicha umumiy savdo hajmi
total_sales = df2.iloc[:, 1:].sum()

# 2. Eng yuqori umumiy savdoli sana
df2["Total_Sales"] = df2.iloc[:, 1:].sum(axis=1)
highest_sales_date = df2.loc[df2["Total_Sales"].idxmax(), "Date"]

# 3. Kunlik foiz o‘zgarishni hisoblash
df2.iloc[:, 1:4] = df2.iloc[:, 1:4].pct_change() * 100

# 4. Sotuvlar tendensiyasini chizish
df2.set_index("Date").plot(kind='line', marker='o', figsize=(10, 5))
plt.ylabel("Savdo hajmi")
plt.title("Mahsulotlarning kunlik savdo tendensiyasi")
plt.show()

print("Eng ko‘p sotilgan sana:", highest_sales_date)



data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# 1. Har bir bo'lim bo'yicha o'rtacha maosh
avg_salary_by_department = df3.groupby("Department")["Salary"].mean()

# 2. Eng tajribali xodim
most_experienced_employee = df3.loc[df3["Experience (Years)"].idxmax()]

# 3. Maoshning minimal maoshga nisbatan o'sishi
df3["Salary Increase"] = ((df3["Salary"] - df3["Salary"].min()) / df3["Salary"].min()) * 100

# 4. Bo‘limlar bo‘yicha xodimlar taqsimoti
df3["Department"].value_counts().plot(kind="bar", color='purple')
plt.xlabel("Bo‘limlar")
plt.ylabel("Xodimlar soni")
plt.title("Bo‘limlar bo‘yicha xodimlar taqsimoti")
plt.show()

print("Eng tajribali xodim:")
print(most_experienced_employee)




data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# 1. Umumiy daromad hisoblash
total_revenue = df4["Total_Price"].sum()

# 2. Eng ko‘p buyurtma qilingan mahsulot
most_ordered_product = df4["Product"].value_counts().idxmax()

# 3. O'rtacha buyurtma hajmini hisoblash
avg_quantity = df4["Quantity"].mean()

# 4. Mahsulotlar bo‘yicha savdolar taqsimoti
df4.groupby("Product")["Total_Price"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Mahsulotlar bo‘yicha umumiy daromad taqsimoti")
plt.show()

print("Eng ko‘p buyurtma qilingan mahsulot:", most_ordered_product)
print("Umumiy daromad:", total_revenue)
print("O‘rtacha buyurtma hajmi:", avg_quantity)
