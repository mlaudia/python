import unittest
from circle import Circle
from math import pi


class TestCircle(unittest.TestCase):

    def testRepr(self):
        self.assertEqual(repr(Circle(1, 2, 3)), "Circle(1, 2, 3)")

    def testEq(self):
        self.assertTrue(Circle(1, 2, 3) == Circle(1, 2, 3))

    def testNe(self):
        self.assertFalse(Circle(1, 2, 3) == Circle(1, 5, 4))

    def testArea(self):
        self.assertEqual(Circle(1,2,3).area(), pi*9)

    def testMove(self):
        self.assertEqual(Circle(1,2,3).move(2, 3), Circle(3, 5, 3))

    def testCover(self):
        self.assertEqual(Circle(1, 2, 2).cover(Circle(6, 2, 1)), Circle(3.5, 2, 7))
    




if __name__ == '__main__':
    unittest.main()