from Library import Library
from Book import Book
from Magzine import Magazine
from CD import CD


# Demonstration
library = Library()

# Add items to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780743273565")
magazine1 = Magazine("National Geographic", "Various", 2022, "April")
cd1 = CD("Abbey Road", "The Beatles", 1969, "Rock")

library.add_item(book1)
library.add_item(magazine1)
library.add_item(cd1)

# Display all items in the library
library.display_all_items()

# Search for items in the library
library.search("beatles")
