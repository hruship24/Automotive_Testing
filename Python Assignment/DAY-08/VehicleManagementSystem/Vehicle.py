class Vehicle:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def display_info(self):
        print("Make:", self._make)
        print("Model:", self._model)
        print("Year:", self._year)
