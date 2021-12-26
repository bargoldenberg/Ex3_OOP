from unittest import TestCase
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time
sys.path.append(os.path.abspath(os.path.join('..', 'data')))


class testGraphAlgo(unittest.TestCase):
    # ten_nodes = os.path.join(os.path.abspath(os.path.join('..','..', 'data','10Nodes.json')))
    # one_hundred_nodes = os.path.join(os.path.abspath(os.path.join('..','..', 'data','100Nodes.json')))
    # one_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..','..', 'data','1000Nodes.json')))
    # ten_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..','..', 'data','10000Nodes.json')))
    # one_hundred_thousand_nodes = os.path.join(os.path.abspath(os.path.join('..','..', 'data','100000Nodes.json')))
    # def test_10_nodes_buildgraph(self):
    #
    #     start = time.time()
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_nodes)
    #     end = time.time()
    #     print("10 Nodes 90 Edges: "+str(end-start)+" s")
    #
    # def test_100_nodes_buildgraph(self):
    #     start = time.time()
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_nodes)
    #     end = time.time()
    #     print("100 Nodes 9000 Edges: "+str(end-start)+" s")
    #
    # def test_1000_nodes_buildgraph(self):
    #     start = time.time()
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_thousand_nodes)
    #     end = time.time()
    #     print("1000 Nodes 90000 Edges: "+str(end-start)+" s")
    #
    # def test_10000_nodes_buildgraph(self):
    #     start = time.time()
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_thousand_nodes)
    #     end = time.time()
    #     print("10000 Nodes 900000 Edges: "+str(end-start)+" s")
    # def test_100000_nodes_buildgraph(self):
    #     start = time.time()
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_thousand_nodes)
    #     end = time.time()
    #     print("100000 Nodes 9000000 Edges: "+str(end-start)+" s")

    # def test_10_nodes_shortest_path(self):
    #     print('ShortestPath')
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_nodes)
    #     start = time.time()
    #     g.shortest_path(5, 6)
    #     end = time.time()
    #     print("10 Nodes 90 Edges: "+str(end-start)+" s")
    #
    # def test_100_nodes_shortest_path(self):
    #
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_nodes)
    #     start = time.time()
    #     g.shortest_path(5,6)
    #     end = time.time()
    #     print("100 Nodes 9000 Edges: "+str(end-start)+" s")
    #
    # def test_1000_nodes_shortest_path(self):
    #
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_thousand_nodes)
    #     start = time.time()
    #     g.shortest_path(5,6)
    #     end = time.time()
    #     print("1000 Nodes 90000 Edges: "+str(end-start)+" s")
    #
    # def test_10000_nodes_shoretest_path(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_thousand_nodes)
    #     start = time.time()
    #     g.shortest_path(5,6)
    #     end = time.time()
    #     print("10000 Nodes 900000 Edges: "+str(end-start)+" s")

    # def test_100000_nodes_shortest_path(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_thousand_nodes)
    #     start = time.time()
    #     g.shortest_path(5,6)
    #     end = time.time()
    #     print("100000 Nodes 9000000 Edges: "+str(end-start)+" s")

    # def test_10_nodes_center_point(self):
    #     print('CenterPoint')
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_nodes)
    #     start = time.time()
    #     g.centerPoint()
    #     end = time.time()
    #     print("10 Nodes 90 Edges: " + str(end - start) + " s")
    #
    # def test_100_nodes_center_point(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_nodes)
    #     start = time.time()
    #     g.centerPoint()
    #     end = time.time()
    #     print("100 Nodes 9000 Edges: " + str(end - start) + " s")
    #
    # def test_1000_nodes_center_point(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_thousand_nodes)
    #     start = time.time()
    #     g.centerPoint()
    #     end = time.time()
    #     print("1000 Nodes 90000 Edges: " + str(end - start) + " s")

    '''
    all of these tests took more than 1 min
    '''
    # def test_10000_nodes_center_point(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_thousand_nodes)
    #     start = time.time()
    #     g.centerPoint()
    #     end = time.time()
    #     print("10000 Nodes 900000 Edges: " + str(end - start) + " s")
    #
    # def test_100000_nodes_center_point(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_thousand_nodes)
    #     start = time.time()
    #     g.shortest_path(5, 6)
    #     end = time.time()
    #     print("100000 Nodes 9000000 Edges: " + str(end - start) + " s")

    # def test_10_nodes_TSP(self):
    #     print('TSP')
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_nodes)
    #     start = time.time()
    #     g.TSP([1,2,3])
    #     end = time.time()
    #     print("10 Nodes 90 Edges: "+str(end-start)+" s")
    #
    # def test_100_nodes_TSP(self):
    #
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_nodes)
    #     start = time.time()
    #     g.TSP([1,2,3])
    #     end = time.time()
    #     print("100 Nodes 9000 Edges: "+str(end-start)+" s")
    #
    # def test_1000_nodes_TSP(self):
    #
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_thousand_nodes)
    #     start = time.time()
    #     g.TSP([1,2,3])
    #     end = time.time()
    #     print("1000 Nodes 90000 Edges: "+str(end-start)+" s")
    #
    # def test_10000_nodes_TSP(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.ten_thousand_nodes)
    #     start = time.time()
    #     g.TSP([1,2,3])
    #     end = time.time()
    #     print("10000 Nodes 900000 Edges: "+str(end-start)+" s")

    # def test_100000_nodes_TSP(self):
    #     g = GraphAlgo()
    #     g.load_from_json(self.one_hundred_thousand_nodes)
    #     start = time.time()
    #     g.TSP([1,2,3])
    #     end = time.time()
    #     print("100000 Nodes 9000000 Edges: "+str(end-start)+" s")


