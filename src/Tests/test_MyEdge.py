from unittest import TestCase
from src.MyEdge import MyEdge


class TestMyEdge(TestCase):

    def test_get_src(self):
        e1 = MyEdge(0,5,4)
        e2 = MyEdge(1, 7, 3)
        e3 = MyEdge(2, -5, 88)
        self.assertEqual(0, e1.getSrc())
        self.assertEqual(1, e2.getSrc())
        self.assertEqual(2, e3.getSrc())

    def test_get_dest(self):
        e1 = MyEdge(0, 5, 4)
        e2 = MyEdge(1, 7, 3)
        e3 = MyEdge(2, -5, 88)
        self.assertEqual(5, e1.getDest())
        self.assertEqual(7, e2.getDest())
        self.assertEqual(-5, e3.getDest())

    def test_get_weight(self):
        e1 = MyEdge(0, 5, 4)
        e2 = MyEdge(1, 7, -3/2)
        e3 = MyEdge(2, -5, 3.1415926535)
        self.assertEqual(4, e1.getWeight())
        self.assertEqual( -3/2, e2.getWeight())
        self.assertEqual(3.1415926535, e3.getWeight())

    def test_get_key(self):
        e1 = MyEdge(0, 5, 4)
        e2 = MyEdge(1, 7, -3 / 2)
        e3 = MyEdge(2, -5, 3.1415926535)
        self.assertEqual([0,5], e1.getKey())
        self.assertEqual([1,7], e2.getKey())
        self.assertEqual([2,-5], e3.getKey())
