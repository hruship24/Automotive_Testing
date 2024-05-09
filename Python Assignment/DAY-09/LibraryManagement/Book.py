from Item import Item


class Book(Item):
    def __init__(self, title, author, publication_year, isbn):   # International Standard Book Number (ISBN)
        super().__init__(title, author, publication_year)
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print("ISBN:", self.isbn)
