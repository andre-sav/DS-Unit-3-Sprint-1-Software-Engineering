import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):

    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""

        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product price being 10."""

        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_steal_explode(self):
        prod1 = Product('Test 1')
        prod1.price = 50
        prod1.weight = 95
        prod2 = Product('Test 2')
        prod2.flammability = 2.4
        prod2.weight = 79
        self.assertEqual(prod1.stealability(), 'Kinda stealable.')
        self.assertEqual(prod2.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)


if __name__ == '__main__':
    unittest.main()
