import unittest
from creditcardexpiry import *

class creditcardvalidation(unittest.TestCase):

    def setUp(self):
        print("setup")

    def test_validateccexpire_valid(self):
        result=validateccexpire(date(2024,5,22))
        self.assertEqual("valid",result)

    def test_validateccexpire_expired(self):
        with self.assertRaises(RuntimeError):
            validateccexpire(date(2020,5,22))
        #self.assertEqual("expired",result)

    def tearDown(self):
        print("teardown")

if __name__=="__main__":
    unittest.main()