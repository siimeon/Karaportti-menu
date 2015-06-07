from unittest import TestCase
from amica import price_modification


class TestPriceModification(TestCase):

    def test_price_modification(self):
        original_string = "Nokia 6,20 \u20ac/6,65 \u20ac Ext 8,90 \u20ac/9,20 \u20ac"
        modified_prices = {"Price": "8,90 \u20ac",
                           "Nokia Price": "6,20 \u20ac"}
        self.assertEqual(price_modification(original_string), modified_prices)

    def test_with_salad_price(self):
        original_string = "Nokia 16,40 \u20ac/kg Ext 16,40 \u20ac/kg"
        modified_price = {"Nokia Price": "16,40 \u20ac/kg",
                          "Price": "16,40 \u20ac/kg"}
        self.assertEqual(price_modification(original_string), modified_price)

