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
    '''
    two Helpers for TCP:
    1.smallest_dist - gets array of distances(flout) and return the index(!!) of the smallest.
    2.total_weight - get a list of paths(as ints - representing the id's), and return the total weight according to the order of the list.
    '''

    def smallest_dist(self,distance_list):
        index_of_smallest = 0
        smallest =distance_list[0]
        for i in range(len(distance_list)):
            if distance_list[i] < smallest:
                smallest = distance_list[i]
                index_of_smallest = i
        return index_of_smallest
    def total_weight(self,cities: List):
        weight = 0.0
        for i in range(len(cities)):
            if i < len(cities)-1:
                weight += self.shortest_path(cities[i],cities[i+1])[-2]
        return weight


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        all_path = []
        index = 0
        my_dist = []
        flag = True
        # First, check if the sub graph (all the nodes on the list) is connected.
        path_check = 0
        for i in range(len(node_lst)):
            if i != 0:
                path_check = self.shortest_path(node_lst[0], node_lst[i])[-2]
                if path_check <= 0:
                    flag = False
        for i in range(len(node_lst)):
            if i != 0:
                path_check = self.shortest_path(node_lst[i],node_lst[0])[-2]
                if path_check <= 0:
                    flag = False
        if flag is False:
            return None
        else:
            for num in range(len(node_lst)):
                curr = num
                rightOrder = []
                tmp = 0
                counter = 0
                distance =[]
                ptr = self.g._V.get(curr)
                rightOrder.append(ptr)
                while counter<len(node_lst) and len(rightOrder)< len(node_lst):
                    ptr = self.g._V.get(curr)
                    tmp = curr
                    for i in range(len(node_lst)):
                        if ptr.get_key() is not node_lst[i]:
                            distance.append(self.shortest_path(ptr.get_key(),node_lst[i]))
                        else:
                            distance.append(self.shortest_path(ptr.get_key(),node_lst[i]))
                    while curr is tmp:
                        smallest = self.smallest_dist(distance)
                        if smallest not in rightOrder:
                            rightOrder.append(smallest)
                            curr = smallest
                            counter += 1
                        elif len(rightOrder) is not len(node_lst):
                            distance[smallest] = float('inf')
                        else:
                            break
                    if len(rightOrder) is len(node_lst):
                        break
                if len(rightOrder) is len(node_lst):
                    all_path.append(rightOrder)
            for i in range(len(all_path)):
                my_dist.append(self.total_weight(all_path[i]))
            index = smallest(my_dist)

            return (all_path[i],my_dist[i])

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