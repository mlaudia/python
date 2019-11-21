import unittest
from point import *

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def testPrint(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(repr(Point(1,2)), "Point(1, 2)")

    def testEq(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(1, 3))

    def testAdd(self):
        self.assertEqual(Point(4, 6), Point(1, 2) + Point(3, 4))

    def testSub(self):
        self.assertEqual(Point(4, 6) - Point(2, 1), Point(2, 5))

    def testMul(self):
        self.assertEqual(Point(2, 3) * Point(3, 4), 18)

    def testCross(self):
        self.assertEqual(Point(1,2).cross(Point(2, 3)), -1)

    def testLength(self):
        self.assertEqual(Point(4, 3).length(), 5)

if __name__ == '__main__':
    unittest.main()