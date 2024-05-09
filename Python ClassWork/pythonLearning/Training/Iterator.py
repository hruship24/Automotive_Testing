#list1 = [10, 20, 30, 40, 50, 60]

# list_itr = iter(list1)
# for i in range(1,len(list1)):
#     print(list_itr.__next__())

# class Ite:
#     def __init__(self):
#         self.count = 0
#
#     def __iter__(self):
#         count = 5
#
#     def __next__(self):
#         if self.count < 10:
#             print(self.count)
#             self.count += 1

class Ite:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 10:
            value = self.count
            self.count += 1
            return value
        else:
            return None  # Return None when there are no more elements

it = Ite()
for i in it:
    print(i)
it = Ite()
for i in it:
    if i is not None:
        print(i)
    else:
        break