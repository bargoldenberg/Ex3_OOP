


import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
from src.DiGraph import DiGraph
from src.MyEdge import MyEdge
class TestDiGraph(unittest.TestCase):
    def test_v_size(self):
        g=DiGraph()
        size=g.v_size()
        self.assertEqual(size,0)
        g.add_node(5,(1,2,3))
        size = g.v_size()
        self.assertEqual(size, 1)
        
    def test_e_size(self):
        g = DiGraph()
        size = g.e_size()
        self.assertEqual(size,0)
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        g.add_edge(5,3,10)
        size = g.e_size()
        self.assertEqual(1,size)
        
    def test_get_all_v(self):
        g = DiGraph()
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        v = g.get_all_v()
        size = len(v)
        self.assertEqual(size,2)

    def test_all_edges_of_node(self):
        g = DiGraph()
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        g.add_edge(5, 3, 10)
        dict={5:10}
        edges = g.all_in_edges_of_node(3)
        self.assertEqual(dict,edges)

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        g.add_edge(5, 3, 10)
        dict={3:10}
        edges = g.all_out_edges_of_node(5)
        self.assertEqual(dict,edges)

    def test_get_mc(self):
        g = DiGraph()
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        g.add_edge(5, 3, 10)
        MC = g.get_mc()
        self.assertEqual(3,MC)
        
    def test_add_edge(self):
        g = DiGraph()
        size = g.e_size()
        self.assertEqual(size, 0)
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        g.add_edge(5, 3, 10)
        size = g.e_size()
        E = g.get_all_e()
        self.assertEqual(1, size)
        edge = MyEdge(5,3,10)
        edge1 = E.get('5,3')
        self.assertEqual(edge.getSrc(),edge1.getSrc())
        self.assertEqual(edge.getDest(), edge1.getDest())
        self.assertEqual(edge.getWeight(), edge1.getWeight())

    def test_add_node(self):
        g=DiGraph()
        g.add_node(5,(1,2,3))
        size = g.v_size()
        self.assertEqual(size, 1)

    def test_remove_node(self):
        g = DiGraph()
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        g.add_edge(5, 3, 10)
        g.remove_node(3)
        v = g.get_all_v()
        self.assertFalse(3 in v)
        size = len(v)
        self.assertEqual(size,1)
        e = g.get_all_e()
        size = len(e)
        self.assertEqual(0,size)

    def test_remove_edge(self):
        g = DiGraph()
        g.add_node(5, (1, 2, 3))
        g.add_node(3, (1, 1, 3))
        g.add_edge(5, 3, 10)
        e = g.get_all_e()
        self.assertTrue('5,3' in e)
        g.remove_edge(5,3)
        e = g.get_all_e()
        self.assertFalse('5,3' in e)

if __name__ == '__main__':
    unittest.main()