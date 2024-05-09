class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in the library.")

    def display_all_items(self):
        print("All Items in the Library:")
        for item in self.items:
            item.display_info()

    def search(self, keyword):
        print("Search results for keyword '{}'".format(keyword))
        for item in self.items:
            if keyword.lower() in item.title.lower() or keyword.lower() in item.author.lower():
                item.display_info()
