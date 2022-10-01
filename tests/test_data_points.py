import unittest
from colorama import Fore


class TestDataPoints(unittest.TestCase):
    def test_data_points(self):
        self.assertEqual(1, 1)
    
    @classmethod
    def setUpClass(cls):
        print(Fore.YELLOW + "Start test for DataPoints class" + Fore.RESET)
        
    @classmethod
    def tearDownClass(cls):
        print(Fore.GREEN + "End test for DataPoints class" + Fore.RESET)
