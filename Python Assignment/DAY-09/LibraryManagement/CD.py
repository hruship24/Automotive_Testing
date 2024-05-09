from Item import Item


class CD(Item):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print("Genre:", self.genre)
