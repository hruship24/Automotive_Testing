class Generator:
    def my_generator(data):
        for item in data:
            yield item

    my_gen = my_generator([1, 2, 3, 4, 5, 6])

    for item in my_gen:
        print(item)