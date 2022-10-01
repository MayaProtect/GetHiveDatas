import unittest
from colorama import Fore


class TestRequestMaker(unittest.TestCase):
    def test_request_maker(self):
        self.assertEqual(1, 1)

    @classmethod
    def setUpClass(cls):
        print(Fore.YELLOW + "Start test for RequestMaker class" + Fore.RESET)

    @classmethod
    def tearDownClass(cls):
        print(Fore.GREEN + "End test for RequestMaker class" + Fore.RESET)
