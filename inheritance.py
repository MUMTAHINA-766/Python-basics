class Robot:

    def __init__(self,name,version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f'{self.name} is moving forward!')

    def move_backward(self):
        print(f'{self.name} is moving backward!')

    def move_right(self):
        print(f'{self.name} is moving right!')

    def move_left(self):
        print(f'{self.name} is moving left!')

class HouseBot(Robot):
    pass

hBot = HouseBot('hBot', 1.1)
print(hBot.name)
hBot.move_forward()