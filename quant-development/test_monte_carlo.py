import unittest
from monte_carlo_functions import simulate_stock_price

class TestMonteCarlo(unittest.TestCase):

    def test_simulate_stock_price_length(self):
        starting_price = 100
        days = 252
        mean_daily_return = 0.0003
        daily_volatility = 0.02

        prices = simulate_stock_price(starting_price, days, mean_daily_return, daily_volatility)
        self.assertEqual(len(prices), days + 1, "The length of prices should be equal to days + 1")

    def test_simulate_stock_price_starting_price(self):
        starting_price = 100
        days = 252
        mean_daily_return = 0.0003
        daily_volatility = 0.02

        prices = simulate_stock_price(starting_price, days, mean_daily_return, daily_volatility)
        self.assertEqual(prices[0], starting_price, "The first price should be equal to the starting price")
