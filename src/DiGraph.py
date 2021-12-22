
from MyEdge import *
from MyNode import *
import random

class DiGraph :
    def __init__(self):
        self._V = {}
        self._E = {}
        self._MC = 0

    def v_size(self) -> int:
        return len(self._V)

    def e_size(self) -> int:
        return len(self._E)

    def get_all_v(self) -> dict:
        return self._V.copy()

    def all_in_edges_of_node(self, id1: int) -> dict:
        #node = MyNode()
        node = self._V.get(id1)
        list = node.get_in_edges().copy()
        dict = {}
        for src in list:
           # e = MyEdge()
            e = self._E.get(str(int(src))+","+str(node.get_key()))
            dict[int(src)] = e.getWeight()
        return dict

    def all_out_edges_of_node(self, id1: int) -> dict:
        node = self._V.get(id1)
        if node.get_out_edges() is not None:
            list = node.get_out_edges().copy()
            dict = {}
            for dest in list:
                e = self._E.get(str(node.get_key())+","+str(int(dest)))
                dict[dest] = e.getWeight()
            return dict
        else:
            return None

    def get_mc(self) -> int:
        return self._MC

    def get_all_e(self):
        return self._E.copy()

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        e = MyEdge(id1, id2,weight)
        if id1 in self._V and id2 in self._V:
            self._E[e.getKey()]=e
            self._V.get(id1).add_edge_list(e)
            self._V.get(id2).add_edge_list(e)
            self._MC += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos == None:
            node = MyNode(random.random()*10, random.random()*10, node_id, 0)
        else:
            node = MyNode(pos[0],pos[1],node_id,0)
        self._V[node_id]=node
        self._MC+=1

    def remove_node(self, node_id: int) -> bool:
        if not node_id in self._V:
            return False
        else:
            if self._V.get(node_id).get_in_edges() is None:
                in_size=0
            else:
                in_size = len(self._V.get(node_id).get_in_edges())
            if self._V.get(node_id).get_out_edges() is None:
                out_size=0
            else:
                out_size = len(self._V.get(node_id).get_out_edges())
            for i in range(in_size):
                self.remove_edge(self._V.get(node_id).get_in_edges()[i],self._V.get(node_id).get_key())
            for i in range(out_size):
                self.remove_edge(self._V.get(node_id).get_key(),self._V.get(node_id).get_out_edges()[i])
            self._V.pop(node_id)
            self._MC += 1
            return True





    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        key = str(node_id1)+","+str(node_id2)
        self._V.get(node_id1).remove_edge_list(node_id1,node_id2)
        self._E.pop(key)


    def __repr__(self):
        return f" Edges {self._E}, Vertecies {self._V}"
    #Bar's...
    def connectinit(self, edge):
        self._V.get(edge.getSrc()).add_edge_list(edge)
        self._V.get(edge.getDest()).add_edge_list(edge)
        key = str(edge.getSrc())+","+str(edge.getDest())
        self._E[key]=edge
        self._MC+=1