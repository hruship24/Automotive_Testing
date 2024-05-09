class ShoppingCart:
    def _init_(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        items = {}
        if product_id in items:
            items[product_id] += quantity
        else:
            items[product_id] = quantity
        return items

    def remove_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] -= quantity
            if self.items[product_id] <= 0:
                del self.items[product_id]

    def update_quantity(self, product_id, new_quantity):
        if product_id in self.items:
            self.items[product_id] = new_quantity

    def calculate_subtotal(self, product_prices):
        subtotal = 0
        for product_id, quantity in self.items.items():
            subtotal += product_prices[product_id] * quantity
        return subtotal
