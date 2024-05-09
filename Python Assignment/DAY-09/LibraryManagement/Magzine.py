from Item import Item


class Magazine(Item):
    def __init__(self, title, author, publication_year, issue_number):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.issue_number)
