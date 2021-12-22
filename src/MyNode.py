import numpy as np
from MyEdge import *

class MyNode:
    def __init__(self,x,y,key,weight):
        self._pos = (x,y,0.0)
        self._key=key
        self._weight=weight
        self._out_edges = None
        self._in_edges = None

    def get_key(self):
        return self._key

    def set_key(self,key):
        self._key=key

    def set_pos(self,pos):
        self._pos = pos

    def get_pos(self):
        return self._pos

    def get_weight(self):
        return self._weight

    def set_weight(self,weight):
        self._weight=weight

    def set_in_edges(self,list_edges):
        self._in_edges=list_edges

    def set_out_edges(self,list_edges):
        self._out_edges=list_edges
    def get_in_edges(self):
        return self._in_edges

    def get_out_edges(self):
        return self._out_edges

    def add_edge_list(self, edge):
        if edge.getSrc()==self._key:
            if self._out_edges is None:
                self._out_edges=np.array([])
            self._out_edges=np.append(self._out_edges,edge.getDest())
            #self._out_edges.append(edge.getDest())
            return True
        elif edge.getDest()==self._key:
            if self._in_edges is None:
                self._in_edges=np.array([])
            self._in_edges = np.append(self._in_edges, edge.getSrc())
            #self._in_edges.append(edge.getSrc())
            return True
        else:
            return False
    def remove_edge_list(self,src,dest):
        if src == self._key:
            if dest in self._out_edges:
                indx = np.where(self._out_edges==dest)
                self._out_edges = np.delete(self._out_edges,indx)
                #self._out_edges.remove(dest)
            return True
        elif dest == self._key:
            if src in self._in_edges:
                self._in_edges.remove(src)
            return True
        else:
            return False

    def __repr__(self):
        return f"Location: {self._pos}, Key = {self._key}"





