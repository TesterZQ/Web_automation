'''
入口函数

'''
import HTMLTestRunnerNew
import unittest

from  TestCase import test_login
from TestCase.invest import test_invest

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.TestLoader().loadTestsFromModule(test_invest))
    # suite.addTest(unittest.TestLoader().loadTestsFromModule(test_login))
    # with open(path.testreport_path,'wb+') as file:
    #     runner=HTMLTestRunnerNew.HTMLTestRunner(file,tester='ZQ',verbosity=2)
    #     runner.run(suite)
    suit = unittest.TestSuite()
    suit.addTest(unittest.TestLoader().loadTestsFromModule(test_invest))
    suit.addTest(unittest.TestLoader().loadTestsFromModule(test_login))
    with open('Web_V2.HTML', 'wb+') as file:
        b = HTMLTestRunnerNew.HTMLTestRunner(file,tester='ZQ',verbosity=2)
        b.run(suit)

