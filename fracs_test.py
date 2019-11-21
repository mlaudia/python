import unittest
from fracs import *

class TestFractions(unittest.TestCase):
    def setUp(self): pass

    def testAdd(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 4), Frac(3, 4))

    def testSub(self):
        self.assertEqual(Frac(3,4) - Frac(1,2), Frac(1, 4))

    def testMul(self):
        self.assertEqual(Frac(1, 2) * Frac(2, 5), Frac(1, 5))

    def testDiv(self):
        self.assertEqual(Frac(1,2)/Frac(5,2), Frac(1,5))

    def testPrint(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(2, 1)), "2")
        self.assertEqual(repr(Frac(1,2)), "Frac(1, 2)")
    
    def testFloat(self):
        self.assertEqual(float(Frac(1,2)), 0.5)
    
    def testComparison(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertTrue(Frac(1, 2) != Frac(1, 5))
        self.assertTrue(Frac(1, 20) < Frac(1, 2))
        self.assertTrue(Frac(1, 3) > Frac(1, 3000))
        self.assertTrue(Frac(1, 2) >= Frac(2, 4))
        self.assertTrue(Frac(3, 6) <= Frac(1, 2))
        

if __name__ == '__main__':
    unittest.main()