import unittest
import sys
import os
path = sys.path.append(os.path.abspath(os.path.join('..','..','src')))
path1 = ''
path = path1
from src.DiGraph import DiGraph
from src.GraphAlgo import *
import datetime


class MyTestCase(unittest.TestCase):

    '''
    still doesnt wort perfectly (line 23 - remove_node).
    '''
    def test_save_load_get(self):
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\A0.json')
        self.assertEqual(11,g.get_graph().v_size())
        self.assertEqual(22,g.get_graph().e_size())
        gr = g.get_graph()
        gr.remove_node(10)
        g.__init__(gr)
        self.assertEqual(10, g.get_graph().v_size())
        self.assertEqual(18, g.get_graph().e_size())

    def test_shortest_path(self):
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\A0.json')
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
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\isCon_test1.json')
        self.assertFalse(g.isConnected())
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\isCon_test2.json')
        self.assertTrue(g.isConnected())
        '''
            RunTime test (for 1000 nodes Graph):
        '''
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\1000Nodes.json')
        start = datetime.datetime.now()
        g.isConnected()
        end = datetime.datetime.now()
        duraction = (end - start)
        duraction.total_seconds()
        self.assertTrue(duraction.total_seconds() < 1)
        '''
            RunTime test (for 10000 nodes Graph):
        '''
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\10000Nodes.json')
        start = datetime.datetime.now()
        g.isConnected()
        end = datetime.datetime.now()
        duraction = (end - start)
        duraction.total_seconds()
        self.assertTrue(duraction.total_seconds() < 3)

    def test_centerPoint(self):
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\A0.json')
        self.assertTrue(7,g.centerPoint()[-2])
        '''
            RunTime test (for 1000 nodes Graph):
        '''
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\1000Nodes.json')
        start = datetime.datetime.now()
        g.centerPoint()
        end = datetime.datetime.now()
        duraction = (end - start)
        duraction.total_seconds()
        self.assertTrue(duraction.total_seconds() < 30)
        '''
            RunTime test (for 10000 nodes Graph): // NOT RECOMMENDED FOR SLOW COMPUTERS!! 
        '''
        # g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\10000Nodes.json')
        start = datetime.datetime.now()
        g.centerPoint()
        end = datetime.datetime.now()
        duraction = (end - start)
        duraction.total_seconds()
        self.assertTrue(duraction.total_seconds() < 1500)

    def test_TSP(self):
        gr = DiGraph()
        g = GraphAlgo(gr)
        g.load_from_json(r'C:\Users\sappi\PycharmProjects\Ex3_OOP\data\Tsp_test.json')
        a = g.TSP([0,2])
        print('printing:')
        print(a)
        # self.assertEqual([0,1,2],g.TSP([0,2])[-1])




if __name__ == '__main__':
    unittest.main()
