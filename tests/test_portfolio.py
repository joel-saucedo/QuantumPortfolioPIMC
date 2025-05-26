import unittest
from src.quantum.portfolio import Portfolio

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_initialization(self):
        self.assertIsNotNone(self.portfolio)

    def test_add_asset(self):
        self.portfolio.add_asset('AAPL', 10)
        self.assertIn('AAPL', self.portfolio.assets)
        self.assertEqual(self.portfolio.assets['AAPL'], 10)

    def test_remove_asset(self):
        self.portfolio.add_asset('AAPL', 10)
        self.portfolio.remove_asset('AAPL')
        self.assertNotIn('AAPL', self.portfolio.assets)

    def test_optimize_portfolio(self):
        self.portfolio.add_asset('AAPL', 10)
        self.portfolio.add_asset('GOOGL', 5)
        optimized = self.portfolio.optimize()
        self.assertIsNotNone(optimized)

if __name__ == '__main__':
    unittest.main()