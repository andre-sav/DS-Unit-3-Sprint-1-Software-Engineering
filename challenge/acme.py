import random


class Product:

    price = 10

    weight = 20

    flammability = 0.5

    identifier = random.randint(1000000, 9999999)

    def __init__(self, name):

        self.name = name

    def stealability(self):

        var = self.price / self.weight
        if var < 0.5:
            return 'Not so stealable...'
        elif var >= 0.5 and var < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):

        var = self.flammability * self.weight
        if var < 10:
            return 'fizzle.'
        elif var >= 10 and var < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    weight = 10

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
