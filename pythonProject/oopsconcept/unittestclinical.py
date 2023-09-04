import unittest
from clinical import *

class unittestclinicaldata(unittest.TestCase):
    def setUp(self):
        print("Set up")

    def test_clinical_validobject(self):
        p1 = patient("john", "34")
        c1 = component("BP", "80")
        p1.adddata(c1)
        c2 = component("Heartrate", "120")
        p1.adddata(c2)
        self.assertEqual("john",p1.name)
        self.assertEqual("34", p1.age)
        list=["80","120"]

        for eachcomponent in p1.component:
                for each in list:
                    self.assertEqual(each,eachcomponent.rating)
                    print(each)

    def tearDown(self):
        print("teardown")

if __name__ == "__main__":
    unittest.main()
