from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']

NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = ADJECTIVES[random.randint(0, 4)] + ' ' \
            + NOUNS[random.randint(0, 4)]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        globals()['testProduct' + str(i)] = Product(name)
        globals()['testProduct' + str(i)].price = price
        globals()['testProduct' + str(i)].weight = weight
        globals()['testProduct' + str(i)].flammability = flammability
        products.append(globals()['testProduct' + str(i)])

    return products


def calculate_avg(lst):
    return sum(lst) / len(lst)


def inventory_report(products):
    names = []
    weight = []
    price = []
    flammability = []
    for i in products:
        names.append(i.name)
        weight.append(i.weight)
        price.append(i.price)
        flammability.append(i.flammability)
    print ('ACME CORP INVENTORY REPORT')
    print ('--------------------------')
    print ('unique product names: ', len(set(names)))
    print ('average weight: ', calculate_avg(weight))
    print ('average price: ', calculate_avg(price))
    print ('average flammability: ', calculate_avg(flammability))

if __name__ == '__main__':
    inventory_report(generate_products())