import unittest
from colorama import Fore


class TestResponseDatas(unittest.TestCase):
    def test_response_datas(self):
        self.assertEqual(1, 1)

    @classmethod
    def setUpClass(cls):
        print(Fore.YELLOW + "Start test for ResponseDatas class" + Fore.RESET)

    @classmethod
    def tearDownClass(cls):
        print(Fore.GREEN + "End test for ResponseDatas class" + Fore.RESET)
