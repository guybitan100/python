class Mario():

    def move(self):
        print("I'm moving")


class Shroom():

    def eat_shroom(self):
        print("Now i'm big!")


# Inherits from Mario and Shroom
class BigMario(Mario, Shroom):
    # if you need to add line, but you don't have nothing to add "pass"
    pass


bm = BigMario()
bm.move()
bm.eat_shroom()
