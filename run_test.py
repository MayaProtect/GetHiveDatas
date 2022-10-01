import unittest
from tests import test_data_points, test_request_maker, test_response_datas


def tests():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(test_data_points))
    suite.addTest(loader.loadTestsFromModule(test_request_maker))
    suite.addTest(loader.loadTestsFromModule(test_response_datas))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
    

if __name__ == "__main__":
    tests()
    