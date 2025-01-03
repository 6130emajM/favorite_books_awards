# Welcome message
print("🎭 Welcome to the Annual Book Awards! 🎉")

# Ask the user for their top 3 favorite books
print("\nEnter the titles of your top 3 favorite books.")
books = []
for i in range(1, 4):
    book = input(f"Book {i}: ")
    books.append(book)

# Sort the books alphabetically
books.sort()

# Simulate an award ceremony presentation
print("\n🏆 And now, presenting your favorite books in sorted order:")
for i, book in enumerate(books, start=1):
    print(f"{i}. 📖 {book}")

# Closing message
print("\n✨ Thank you for participating in the Book Awards! Keep reading and enjoying great books! ✨")
