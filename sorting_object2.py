class Toy:
        def __init__(self, name, price):
            self.name = name
            self.price = price
        def sort_priority(self):
         return self.price

def print_toy_object(toy_list):
    for obj in toy_list:
        print(f'Toy: {obj.name}, Price {obj.price}')

toy_1 = Toy('Woody', 1000)
toy_2 = Toy('Aot-wheels', 200)
toy_3 = Toy('b', 10)

toys =  [toy_1, toy_2, toy_3]
#sorting using lambda
toys.sort(key=lambda x: x.price)
print_toy_object(toys)

#sorted using lambda
sorted_toys_again = sorted(toys, key=lambda x:x.price)
print_toy_object(sorted_toys_again)