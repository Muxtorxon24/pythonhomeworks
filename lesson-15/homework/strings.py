#task1
import json

# Read and parse students.json
with open("students.json", "r") as file:
    students = json.load(file)

# Print student details
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

#task2
import requests

API_KEY = "your_openweathermap_api_key"  
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data")

#task3
import json

BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book(title, author, year):
    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print(f"Book '{title}' added successfully!")

def update_book(old_title, new_title, new_author, new_year):
    books = load_books()
    for book in books:
        if book["title"] == old_title:
            book["title"], book["author"], book["year"] = new_title, new_author, new_year
            save_books(books)
            print(f"Book '{old_title}' updated!")
            return
    print("Book not found!")

def delete_book(title):
    books = load_books()
    books = [book for book in books if book["title"] != title]
    save_books(books)
    print(f"Book '{title}' deleted!")
