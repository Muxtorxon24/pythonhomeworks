import pandas as pd

# Ma'lumotlarni yuklash
df = pd.read_csv('task\\stackoverflow.csv')

# 1. 2014-yildan oldin yaratilgan savollar
questions_before_2014 = df[pd.to_datetime(df['creationdate']) < '2014-01-01']
print(questions_before_2014)

# 2. 50 dan yuqori baholangan savollar
high_score_questions = df[df['score'] > 50]
print(high_score_questions)

# 3. 50 dan 100 gacha baholangan savollar
medium_score_questions = df[(df['score'] >= 50) & (df['score'] <= 100)]
print(medium_score_questions)

# 4. Scott Boston javob bergan savollar
scott_boston_questions = df[df['ans_name'] == 'Scott Boston']
print(scott_boston_questions)

# 5. Quyidagi 5 foydalanuvchi javob bergan savollar
users = ['User1', 'User2', 'User3', 'User4', 'User5']
answered_by_users = df[df['ans_name'].isin(users)]
print(answered_by_users)

# 6. 2014-yil mart-oktyabr oralig‘ida Unutbu javob bergan va bahosi 5 dan kam savollar
filtered_questions = df[
    (df['ans_name'] == 'Unutbu') & 
    (df['score'] < 5) & 
    (pd.to_datetime(df['creationdate']).between('2014-03-01', '2014-10-31'))
]
print(filtered_questions)

# 7. Bahosi 5-10 oralig‘ida yoki ko‘rish soni 10,000 dan yuqori bo‘lgan savollar
score_or_views = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print(score_or_views)

# 8. Scott Boston javob bermagan savollar
not_answered_by_scott = df[df['ans_name'] != 'Scott Boston']
print(not_answered_by_scott)


# Ma'lumotlarni yuklash
titanic_df = pd.read_csv("task\\titanic.csv")

# 1. 20-30 yosh orasidagi Class 1 ayol yo'lovchilar
female_class1 = titanic_df[(titanic_df['Sex'] == 'female') & 
                           (titanic_df['Pclass'] == 1) & 
                           (titanic_df['Age'].between(20, 30))]
print(female_class1)

# 2. $100 dan ortiq to‘lov qilgan yo‘lovchilar
high_fare_passengers = titanic_df[titanic_df['Fare'] > 100]
print(high_fare_passengers)

# 3. Yolg‘iz sayohat qilib omon qolgan yo‘lovchilar
alone_survivors = titanic_df[(titanic_df['Survived'] == 1) & 
                             (titanic_df['SibSp'] == 0) & 
                             (titanic_df['Parch'] == 0)]
print(alone_survivors)

# 4. ‘C’ portidan chiqib, $50 dan ortiq to‘lov qilgan yo‘lovchilar
c_port_fare50 = titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50)]
print(c_port_fare50)

# 5. Ham aka-uka yoki turmush o‘rtoqlari, ham ota-onasi yoki farzandlari bo‘lgan yo‘lovchilar
family_travelers = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]
print(family_travelers)

# 6. 15 yosh yoki undan kichik bo‘lib, omon qolmagan yo‘lovchilar
young_non_survivors = titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)]
print(young_non_survivors)

# 7. Kabinasi bor va $200 dan ortiq to‘lov qilgan yo‘lovchilar
cabin_and_high_fare = titanic_df[(titanic_df['Cabin'].notna()) & (titanic_df['Fare'] > 200)]
print(cabin_and_high_fare)

# 8. PassengerId’lari toq son bo‘lgan yo‘lovchilar
odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print(odd_passenger_ids)

# 9. Unikal ticket raqamiga ega yo‘lovchilar
unique_tickets = titanic_df[titanic_df.duplicated(subset='Ticket', keep=False) == False]
print(unique_tickets)

# 10. Ismida ‘Miss’ so‘zi bor va Class 1 da bo‘lgan yo‘lovchilar
miss_class1 = titanic_df[(titanic_df['Sex'] == 'female') & 
                         (titanic_df['Pclass'] == 1) & 
                         (titanic_df['Name'].str.contains('Miss'))]
print(miss_class1)
