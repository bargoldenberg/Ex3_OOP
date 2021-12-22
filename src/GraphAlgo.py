import heapq
import json
from typing import List
from API import GraphInterface
from DiGraph import *
from queue import *
import matplotlib.pyplot as plt
class GraphAlgo:
    """This abstract class represents an interface of a graph."""
    def __init__(self,gr=None):
        if gr is None:
            self.g=DiGraph()
        else:
            self.g = DiGraph()
            V = gr.get_all_v()
            for node in V.values():
                self.g.add_node(node.get_key(),node.get_pos())
            for node in V.values():
                out = gr.all_out_edges_of_node(node.get_key())
                if out is None:
                    continue
                else:
                    for edge in out.keys():
                        self.g.add_edge(int(node.get_key()),int(edge),out[edge])


    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name,"r+")  as f:
                my_d = json.load(f)
                e_dic = my_d["Edges"]
                v_dic = my_d["Nodes"]
                for vertex in v_dic:
                    if 'pos' in vertex.keys():
                        posstring = vertex['pos']
                        poslist = posstring.split(",")
                        zs = poslist.pop()
                        ys = poslist.pop()
                        xs = poslist.pop()
                        x=float(xs)
                        y=float(ys)
                        z=float(zs)
                        self.g.add_node(int(vertex["id"]),(x,y,z))
                    else:
                        self.g.add_node(int(vertex["id"]))
                for edge in e_dic:
                    self.g.add_edge(int(edge["src"]),int(edge["dest"]),float(edge["w"]))

        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        jsondic = {}
        jsondic['Edges'] = []
        jsondic['Nodes'] = []
        edges = self.g.get_all_e()
        for edge in edges.values():
            jsondic['Edges'].append({
                'src': edge.getSrc(),
                'w': edge.getWeight(),
                'dest' : edge.getDest()
            })
        nodes = self.g.get_all_v()
        for node in nodes.values():
            jsondic['Nodes'].append({
                'pos': str(node.get_pos()[0])+','+str(node.get_pos()[1])+','+str(node.get_pos()[2]),
                'id': node.get_key()
            })
        jsonstr = json.dumps(jsondic, indent=2)
        with open(file_name, "w") as outfile:
            outfile.write(jsonstr)


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        distance = {}
        prev = {}
        nodes_queue = []
        heapq.heapify(nodes_queue)
        queueset = {}
        path = []
        v = self.g.get_all_v()
        e = self.g.get_all_e()
        for node in v.values():
            if node.get_key() == id1:
                distance[node.get_key()] = 0.0
                #nodes_queue.put((distance[node.get_key()], node.get_key()))
                heapq.heappush(nodes_queue,(distance[node.get_key()], node.get_key()))
                queueset[node.get_key()]=node.get_key()
            else:
                distance[node.get_key()] = float('inf')
            prev[node.get_key()] = None
        while not len(nodes_queue) == 0:
            #smallest = nodes_queue.get()[1]
            smallest = heapq.heappop(nodes_queue)[1]
            queueset.pop(smallest)
            if smallest == id2:
                while prev[smallest] is not None:
                    path.append(v[smallest].get_key())
                    smallest = prev[smallest]
                path.append(v[smallest].get_key())
                path.reverse()
            elif distance[smallest] == float('inf'):
                break;
            else:
                if v[smallest].get_out_edges() is None:
                    return (float('inf'),[])
                else:
                    for i in range(len(v[smallest].get_out_edges())):
                        neighbor = e[str(smallest)+','+str(v[v[smallest].get_out_edges()[i]].get_key())]
                        dis = distance[smallest] + neighbor.getWeight()
                        if dis < distance[neighbor.getDest()]:
                            distance[neighbor.getDest()]=dis
                            prev[neighbor.getDest()]=smallest
                            if neighbor.getDest() not in queueset:
                                #nodes_queue.put((distance[neighbor.getDest()],neighbor.getDest()))
                                heapq.heappush(nodes_queue,(distance[neighbor.getDest()],neighbor.getDest()))
                                queueset[neighbor.getDest()]=neighbor.getDest()
        if distance[id2] is not float('inf') and len(path)>0:
            return (distance[id2],path)

    def shortest_path_map(self, id1):
        distance = {}
        prev = {}
        nodes_queue = []
        heapq.heapify(nodes_queue)
        queueset = {}
        v = self.g.get_all_v()
        e = self.g.get_all_e()
        for node in v.values():
            if node.get_key() == id1:
                distance[node.get_key()] = 0.0
                heapq.heappush(nodes_queue, (distance[node.get_key()], node.get_key()))
                queueset[node.get_key()]=node.get_key()
            else:
                distance[node.get_key()] = float('inf')
            prev[node.get_key()] = None
        while not len(nodes_queue)==0:
            smallest = heapq.heappop(nodes_queue)[1]
            queueset.pop(smallest)
            if distance[smallest] == float('inf'):
                break;
            else:
                for i in range(len(v[smallest].get_out_edges())):
                    neighbor = e[str(smallest)+','+str(v[v[smallest].get_out_edges()[i]].get_key())]
                    dis = distance[smallest] + neighbor.getWeight()
                    if dis < distance[neighbor.getDest()]:
                        distance[neighbor.getDest()]=dis
                        prev[neighbor.getDest()]=smallest
                        if neighbor.getDest() not in queueset:
                            heapq.heappush(nodes_queue, (distance[neighbor.getDest()], neighbor.getDest()))
                            queueset[neighbor.getDest()]=neighbor.getDest()

        return distance

    @staticmethod
    def BFS(g,visited, n):
        queue = []
        visited[n]=True
        queue.append(n)
        while not len(queue)==0:
            n=queue.pop()
            out = g.all_out_edges_of_node(n)
            if out is None:
                return
            for key in out.keys():
                if visited[key] is True:
                    continue
                else:
                    visited[key]=True
                    queue.append(key)

    def transpose_graph(self):
        graphT = DiGraph()
        for node in self.g.get_all_v().values():
            graphT.add_node(node.get_key(),node.get_pos())
        for edge in self.g.get_all_e().values():
            graphT.add_edge(edge.getDest(),edge.getSrc(),edge.getWeight())
        return graphT


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
    def isConnected(self):
        visited={}
        v = self.g.get_all_v()
        for vertex in v:
            node = vertex
            visited[vertex]=False
        self.BFS(self.g,visited,node)
        for vertex in v:
            if visited[vertex] is False:
                return False
        for vertex in v:
            visited[vertex]=False
        transposed_graph = self.transpose_graph()
        self.BFS(transposed_graph,visited,node)
        for vertex in v:
            if visited[vertex] is False:
                return False
        return True


    def centerPoint(self) -> (int, float):
        if not self.isConnected():
            return None
        sum_of_dist=[]
        v = self.g.get_all_v()
        for node in v.values():
            distance = self.shortest_path_map(node.get_key())
            eccentricity = -float('inf')
            for ot_node in v.values():
                if ot_node.get_key()==node.get_key():
                    continue
                dist = distance[ot_node.get_key()]
                if dist > eccentricity:
                    eccentricity = dist
            arr = [eccentricity,node.get_key()]
            sum_of_dist.append(arr)
        min = float('inf')
        key = float('inf')
        for i in range(len(sum_of_dist)):
            if sum_of_dist[i][0] < min:
                min = sum_of_dist[i][0]
                key = sum_of_dist[i][1]
        return (key,min)

    def plot_graph(self) -> None:
        v = self.g.get_all_v()
        e = self.g.get_all_e()
        for node in v.values():
            x=node.get_pos()[0]
            y=node.get_pos()[1]
            plt.plot(x,y,markersize = 10,marker="o",color="green")
            plt.text(x,y,str(node.get_key()), color="black",fontsize=12)
        for edge in e.values():
                destx = v[edge.getDest()].get_pos()[0]
                desty = v[edge.getDest()].get_pos()[1]
                srcx = v[edge.getSrc()].get_pos()[0]
                srcy = v[edge.getSrc()].get_pos()[1]
                plt.annotate("",xy=(srcx,srcy),xytext=(destx,desty),arrowprops={'arrowstyle' : "<-",'lw':2})


        plt.show()