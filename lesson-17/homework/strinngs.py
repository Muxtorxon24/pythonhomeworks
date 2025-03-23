########## task 1 ##########
import pandas as pd
import numpy as np

# 1. DataFrame yaratish
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 35, 40], 
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 2. Ustun nomlarini o'zgartirish
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 3. Birinchi 3 qatorni chop etish
print("First 3 rows of DataFrame:")
print(df.head(3))

# 4. O'rtacha yoshni topish
mean_age = df['age'].mean()
print("\nMean Age:", mean_age)

# 5. Faqat 'Name' va 'City' ustunlarini tanlash
print("\nSelected Columns (first_name and City):")
print(df[['first_name', 'City']])

# 6. Yangi 'Salary' ustunini qo'shish
df['Salary'] = np.random.randint(3000, 10000, size=len(df))  # Tasodifiy maosh qo‘shish

# 7. DataFrame statistik ma’lumotlari
print("\nSummary Statistics:")
print(df.describe())



########## task 2 ##########
# 1. DataFrame yaratish
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# 2. Maksimal daromad va xarajatlarni hisoblash
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

# 3. Minimal daromad va xarajatlarni hisoblash
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# 4. O'rtacha daromad va xarajatlarni hisoblash
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)



########## task 3 ##########
# 1. DataFrame yaratish
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# 2. 'Category' ustunini indeks qilish
expenses.set_index('Category', inplace=True)

# 3. Har bir kategoriya uchun maksimal xarajatni topish
print("Maximum expenses per category:")
print(expenses.max(axis=1))

# 4. Har bir kategoriya uchun minimal xarajatni topish
print("\nMinimum expenses per category:")
print(expenses.min(axis=1))

# 5. Har bir kategoriya uchun o'rtacha xarajatni topish
print("\nAverage expenses per category:")
print(expenses.mean(axis=1))
