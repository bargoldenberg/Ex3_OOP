import unittest
import sys
import os
path = sys.path.append(os.path.abspath(os.path.join('..','..','src')))
from src.DiGraph import DiGraph
from src.GraphAlgo import *
import time
import datetime


class MyTestCase(unittest.TestCase):
    A0 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A0.json')))
    A1 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A1.json')))
    A2 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A2.json')))
    A3 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A3.json')))
    A4 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A4.json')))
    A5 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A5.json')))
    '''
    still doesnt wort perfectly (line 23 - remove_node).
    '''
    def test_save_load_get(self):
        A0 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A0.json')))
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(A0)
        self.assertEqual(11,g.get_graph().v_size())
        self.assertEqual(22,g.get_graph().e_size())
        gr = g.get_graph()
        gr.remove_node(10)
        g = GraphAlgo(gr)
        self.assertEqual(10, g.get_graph().v_size())
        self.assertEqual(18, g.get_graph().e_size())

    def test_shortest_path(self):
        A0 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A0.json')))
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(A0)
        test1 = g.shortest_path(1,5)
        test2 = g.shortest_path(7,10)
        self.assertEqual(6.282672154710672, test1[-2])
        self.assertEqual(4.230235452252275, test2[-2])
        '''
            RunTime test:
        '''
        start = datetime.datetime.now()
        test1 = g.shortest_path(1,5)
        end = datetime.datetime.now()
        duraction = (end - start)
        duraction.total_seconds()
        self.assertTrue( duraction.total_seconds() < 0.5)

    def test_isConnected(self):

        tst1 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'isCon_test1.json')))
        tst2 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'isCon_test2.json')))
        ten_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '10Nodes.json')))
        one_hundred_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '100Nodes.json')))
        one_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '1000Nodes.json')))
        ten_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '10000Nodes.json')))
        one_hundred_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '100000Nodes.json')))
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(tst1)
        self.assertFalse(g.isConnected())
        g.load_from_json(tst2)
        self.assertTrue(g.isConnected())
        '''
            RunTime test (for 1000 nodes Graph):
        '''
        g.load_from_json(one_thousand_nodes)
        start = datetime.datetime.now()
        g.isConnected()
        end = datetime.datetime.now()
        duraction = (end - start)
        duraction.total_seconds()
        self.assertTrue(duraction.total_seconds() < 1)
        '''
            RunTime test (for 10000 nodes Graph):
        '''
        g.load_from_json(ten_thousand_nodes)
        start = time.time()
        g.isConnected()
        end = time.time()
        duraction = (end - start)
        self.assertTrue(duraction < 3)

    def test_centerPoint(self):
        A0 = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'A0.json')))
        ten_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '10Nodes.json')))
        one_hundred_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '100Nodes.json')))
        one_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '1000Nodes.json')))
        ten_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '10000Nodes.json')))
        one_hundred_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', '100000Nodes.json')))
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(A0)
        self.assertTrue(7,g.centerPoint()[-2])
        '''
            RunTime test (for 1000 nodes Graph):
        '''
        g.load_from_json(one_thousand_nodes)
        start = datetime.datetime.now()
        g.centerPoint()
        end = datetime.datetime.now()
        duraction = (end - start)
        duraction.total_seconds()
        self.assertTrue(duraction.total_seconds() < 30)
        '''
            RunTime test (for 10000 nodes Graph): // NOT RECOMMENDED FOR SLOW COMPUTERS!! 
        '''
        # g.load_from_json(ten_thousand_nodes)
        # start = datetime.datetime.now()
        # g.centerPoint()
        # end = datetime.datetime.now()
        # duraction = (end - start)
        # duraction.total_seconds()
        # self.assertTrue(duraction.total_seconds() < 1500)

    def test_TSP(self):
        tsptest = os.path.join(os.path.abspath(os.path.join('..', '..', 'data', 'Tsp_test.json')))
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(tsptest)
        a = g.TSP([0,2])
        print('printing:')
        print(a)
        # self.assertEqual([0,1,2],g.TSP([0,2])[-1])




if __name__ == '__main__':
    unittest.main()
