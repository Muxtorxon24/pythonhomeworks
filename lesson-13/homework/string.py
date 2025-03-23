from datetime import datetime, date 


#task 1

def yosh_hisobla(tugilgan_sana):
    bugun = date.today()
    tugilgan_sana = datetime.strptime(tugilgan_sana, "%Y-%m-%d").date()

    yillar = bugun.year - tugilgan_sana.year
    oylar = bugun.month - tugilgan_sana.month
    kunlar = bugun.day - tugilgan_sana.day

    if kunlar < 0:
        oylar -= 1
        oldingi_oy = (bugun.month - 1) if bugun.month > 1 else 12
        kunlar += (date(bugun.year, oldingi_oy + 1, 1) - date(bugun.year, oldingi_oy, 1)).days

    if oylar < 0:
        yillar -= 1
        oylar += 12

    return yillar, oylar, kunlar

tugilgan_sana = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
yil, oy, kun = yosh_hisobla(tugilgan_sana)
print(f"Siz {yil} yil, {oy} oy, {kun} kun yashagansiz.")

#task 2

def kun_qolgan(tugilgan_sana):
    bugun = date.today()
    tugilgan_sana = datetime.strptime(tugilgan_sana, "%Y-%m-%d").date()
    
    keyingi_tugilgan_kun = date(bugun.year, tugilgan_sana.month, tugilgan_sana.day)
    
    if keyingi_tugilgan_kun < bugun:
        keyingi_tugilgan_kun = date(bugun.year + 1, tugilgan_sana.month, tugilgan_sana.day)
    
    qolgan_kun = (keyingi_tugilgan_kun - bugun).days
    return qolgan_kun

tugilgan_sana = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
qolgan = kun_qolgan(tugilgan_sana)
print(f"Keyingi tug‘ilgan kuningizgacha {qolgan} kun qoldi.")


#task 3

from datetime import timedelta

current_datetime = input("Hozirgi sana-vaqtni kiriting (YYYY-MM-DD HH:MM): ")
hours = int(input("Uchrashuv davomiyligi (soat): "))
minutes = int(input("Uchrashuv davomiyligi (daqiqalar): "))

current_datetime = datetime.strptime(current_datetime, "%Y-%m-%d %H:%M")
end_datetime = current_datetime + timedelta(hours=hours, minutes=minutes)

print(f"Uchrashuv {end_datetime.strftime('%Y-%m-%d %H:%M')} da tugaydi.")


#task 4
import pytz

datetime_str = input("Sana-vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_timezone = input("Hozirgi vaqt zonangizni kiriting (masalan, Asia/Tashkent): ")
to_timezone = input("Qaysi vaqt zonasiga o‘tkazmoqchisiz? (masalan, UTC): ")

dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_timezone)
to_tz = pytz.timezone(to_timezone)

dt = from_tz.localize(dt).astimezone(to_tz)

print(f"O‘zgartirilgan vaqt: {dt.strftime('%Y-%m-%d %H:%M')} ({to_timezone})")


#task 5
import time
from datetime import datetime

future_time = input("Kelajak sanani kiriting (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_time, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining_time = future_time - now
    if remaining_time.total_seconds() <= 0:
        print("Vaqt tugadi!")
        break
    print(f"Qolgan vaqt: {remaining_time}")
    time.sleep(1)



#task 6
import re

email = input("Email manzilini kiriting: ")
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(pattern, email):
    print("Email manzili to‘g‘ri!")
else:
    print("Email noto‘g‘ri!")




#task 7
phone = input("Telefon raqamingizni kiriting (faqat raqamlar): ")
pattern = r'(\d{3})(\d{3})(\d{4})'

formatted_phone = re.sub(pattern, r'(\1) \2-\3', phone)
print(f"Formatlangan raqam: {formatted_phone}")


#task 8
password = input("Parolni kiriting: ")

length = len(password) >= 8
uppercase = re.search(r'[A-Z]', password)
lowercase = re.search(r'[a-z]', password)
digit = re.search(r'\d', password)
special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

if length and uppercase and lowercase and digit and special_char:
    print("Parol kuchli!")
elif length and uppercase and lowercase and digit:
    print("O‘rtacha kuchli parol.")
else:
    print("Parol juda zaif!")



#task 9
text = input("Matnni kiriting: ")
word = input("Qidirilayotgan so‘zni kiriting: ")

matches = re.findall(rf'\b{word}\b', text, re.IGNORECASE)
print(f"'{word}' so‘zi {len(matches)} marta uchradi.")



#task 10
text = input("Matnni kiriting: ")
pattern = r'\b\d{4}-\d{2}-\d{2}\b'

dates = re.findall(pattern, text)
if dates:
    print("Topilgan sanalar:", ", ".join(dates))
else:
    print("Hech qanday sana topilmadi.")
