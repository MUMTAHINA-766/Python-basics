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

toys = [toy_1, toy_2, toy_3]

#using sort func

toys.sort(key= Toy.sort_priority, reverse=True)
print_toy_object(toys)

#using sorted func

sorted_toys= sorted(toys, key= Toy.sort_priority)
print_toy_object(sorted_toys)