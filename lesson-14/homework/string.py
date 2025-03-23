import json
import requests
import random
import os

def parse_students_json(filepath="students.json"):
    """
    Reads the students.json file and prints details of each student.
    """
    try:
        with open(filepath, "r") as file:
            students = json.load(file)
        print("Student Details:")
        for student in students:
            print(f"Name: {student.get('name')}, Age: {student.get('age')}, Major: {student.get('major')}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

def get_weather(city="Tashkent"):
    """
    Fetches weather data for a given city using the OpenWeatherMap API
    and prints temperature, humidity, and other relevant information.
    """
    API_KEY = "abcdef1234567890abcdef1234567890"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        print(f"Weather for {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather Description: {weather_data['weather'][0]['description']}")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")

def load_books(filepath="books.json"):
    """
    Loads the books from a JSON file. Returns an empty list if file not found.
    """
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            try:
                books = json.load(file)
                return books
            except json.JSONDecodeError:
                print("Error decoding JSON. Starting with an empty list.")
                return []
    else:
        return []

def save_books(books, filepath="books.json"):
    """
    Saves the books list to the JSON file.
    """
    with open(filepath, "w") as file:
        json.dump(books, file, indent=4)

def modify_books(filepath="books.json"):
    """
    Allows users to add new books, update existing book information, and delete books.
    """
    books = load_books(filepath)
    
    def list_books():
        if not books:
            print("No books available.")
        else:
            for idx, book in enumerate(books, start=1):
                print(f"{idx}. Title: {book.get('title')}, Author: {book.get('author')}")
    
    while True:
        print("\nBook Modification Menu:")
        print("1. List Books")
        print("2. Add a New Book")
        print("3. Update a Book")
        print("4. Delete a Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            list_books()
            
        elif choice == "2":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            new_book = {"title": title, "author": author}
            books.append(new_book)
            save_books(books, filepath)
            print("Book added.")
            
        elif choice == "3":
            list_books()
            idx = int(input("Enter the number of the book to update: ")) - 1
            if 0 <= idx < len(books):
                title = input("Enter new title (leave blank to keep current): ").strip()
                author = input("Enter new author (leave blank to keep current): ").strip()
                if title:
                    books[idx]["title"] = title
                if author:
                    books[idx]["author"] = author
                save_books(books, filepath)
                print("Book updated.")
            else:
                print("Invalid book number.")
                
        elif choice == "4":
            list_books()
            idx = int(input("Enter the number of the book to delete: ")) - 1
            if 0 <= idx < len(books):
                deleted = books.pop(idx)
                save_books(books, filepath)
                print(f"Deleted book: {deleted.get('title')}")
            else:
                print("Invalid book number.")
                
        elif choice == "5":
            print("Exiting book modification menu.")
            break
        else:
            print("Invalid choice. Please select from the menu.")

def recommend_movie():
    """
    Asks the user for a movie genre and recommends a random movie from that genre using the OMDB API.
    Note: OMDB API doesn't support direct genre search. This example uses a keyword search.
    """
    API_KEY = "YOUR_OMDB_API_KEY"
    base_url = "http://www.omdbapi.com/"
    
    genre = input("Enter a movie genre (e.g., Comedy, Action, Drama): ").strip()
    
    params = {
        "apikey": API_KEY,
        "s": genre,   
        "type": "movie"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "True" and "Search" in data:
            movies = data["Search"]
            recommended = random.choice(movies)
            print("\nRecommended Movie:")
            print(f"Title: {recommended.get('Title')}")
            print(f"Year: {recommended.get('Year')}")
            print(f"IMDB ID: {recommended.get('imdbID')}")
        else:
            print("No movies found for that genre. Try a different keyword.")
    except requests.RequestException as e:
        print(f"Error fetching movie data: {e}")

def main():
    while True:
        print("\n--- Homework Tasks Menu ---")
        print("1. Parse students.json")
        print("2. Get Weather for Tashkent")
        print("3. Modify books.json")
        print("4. Recommend a Movie")
        print("5. Exit")
        choice = input("Select a task: ").strip()
        
        if choice == "1":
            parse_students_json()
        elif choice == "2":
            get_weather("Tashkent")
        elif choice == "3":
            modify_books()
        elif choice == "4":
            recommend_movie()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    main()
