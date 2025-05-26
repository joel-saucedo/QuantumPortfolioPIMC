import unittest
from src.quantum.pimc import PIMC

class TestPIMC(unittest.TestCase):

    def setUp(self):
        self.pimc = PIMC()

    def test_initialization(self):
        self.assertIsNotNone(self.pimc)

    def test_run_simulation(self):
        result = self.pimc.run_simulation()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, dict))  # Assuming the result is a dictionary

    def test_parameter_management(self):
        params = {'temperature': 300, 'steps': 1000}
        self.pimc.set_parameters(params)
        self.assertEqual(self.pimc.get_parameters(), params)

if __name__ == '__main__':
    unittest.main()