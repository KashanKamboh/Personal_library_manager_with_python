# # library_manager.py

# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="📚 Personal Library Manager", layout="wide")
# st.title("📚 Personal Library Manager")

# # Sample structure for storing book data
# if 'books' not in st.session_state:
#     st.session_state.books = []

# # --- Sidebar: Add a new book ---
# st.sidebar.header("➕ Add a New Book")
# with st.sidebar.form("add_book_form"):
#     title = st.text_input("Title")
#     author = st.text_input("Author")
#     year = st.number_input("Year Published", min_value=0, max_value=2100, step=1)
#     genre = st.text_input("Genre")
#     submitted = st.form_submit_button("Add Book")
    
#     if submitted:
#         if title and author:
#             st.session_state.books.append({
#                 "Title": title,
#                 "Author": author,
#                 "Year": int(year),
#                 "Genre": genre
#             })
#             st.success(f"Book '{title}' added!")
#         else:
#             st.warning("Please fill at least Title and Author.")

# # --- Main area: Display and manage books ---
# st.subheader("📖 Your Book Collection")

# # Search
# search = st.text_input("🔍 Search by title or author").lower()

# # Convert to DataFrame
# df_books = pd.DataFrame(st.session_state.books)

# if not df_books.empty:
#     # Filter
#     if search:
#         df_books = df_books[df_books.apply(lambda row: search in row["Title"].lower() or search in row["Author"].lower(), axis=1)]

#     # Display
#     st.dataframe(df_books, use_container_width=True)

#     # Delete
#     st.subheader("🗑️ Delete a Book")
#     delete_title = st.selectbox("Select a book to delete", df_books["Title"].unique())
#     if st.button("Delete Book"):
#         st.session_state.books = [book for book in st.session_state.books if book["Title"] != delete_title]
#         st.success(f"Deleted '{delete_title}'")
# else:
#     st.info("No books in your library yet. Add some from the sidebar.")

import json
import os

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return[]

def save_library(library):
    with open("data_file", "w") as file:
        json.dump(library,file)

def add_books(library):
    title = input("Enter the tittle of the book")
    author = input("Enter the author of the book")
    year = input("Enter the year of the book")
    genre = input("Enter the genre of the book")
    read = input("Have you read the book? (yes/no)").lower() == "yes"

    new_book = {
        "title" : title,
        "author": author,
        "year": year,
        "genre":genre,
        "read": read
        }
    library.append(new_book)
    save_library(library)
    print(f"Book {title} Added Sucessfully!✨")
def remove_books(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!✨\n")
            return
    print("Book not found.\n")

def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search term: ").strip().lower()
    found = []
    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            found.append(book)
    if found:
        print("Matching Books:")
        for i, book in enumerate(found, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()
    else:
        print("No matching books found.\n")

def display_books(library):
    if not library:
        print("Your Library is empty!")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
                 status = "Read" if book["read"] else "Unread"
                 print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
                 print()

def display_states(library):
     total = len(library)
     if total == 0:
          print("No books are in the library!")
          return
     read_books = sum(1 for book in library if book["read"])
     percent_read = (read_books / total) *100
     print(f"Total Books: {total}")
     print(f"Percentage read: {percent_read}%\n")

def main():
     library = load_library()
     while True:
         print("\n 📚 <<<<<------ Welcome to your Personal Library Manager ----->>>>>>  \n ")
         
         print("1. ➕ Add a book")
         print("2. 🗑️ Remove a book")
         print("3. 🔍 Search for a book")
         print("4. 📖 Display all books")
         print("5. 📊 Display statistics")
         print("6. 🚪 Exit")
         choice = int(input("Enter your choice: "))
         if choice == 1:
               add_books(library)
         elif choice == 2:
               remove_books(library)
         elif choice == 3:
               search_book(library)
         elif choice == 4:
               display_books(library)
         elif choice == 5:
               display_states(library)
         elif choice == 6:
               save_library(library)
               print("Library saved to file. Goodbye!🤗")
               break
         else:
               print("Invalid Choice. Please try again!🙄")

if __name__ == "__main__":
    main()



     





        
        


