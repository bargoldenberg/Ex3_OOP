
class MyEdge:

    # Constructor for edge - that gets all the parameters.
    def __init__(self,src ,dest, weight):
        self._src = src
        self._dest = dest
        self._weight = weight
        self._key = str(src)+","+str(dest)

    # # Copy Constructor for edge - that gets another edge.
    # def __init__(self, edge):
    #     self.src = edge.src
    #     self.dest = edge.src
    #     self.weight = edge.weight
    #     self.keys = edge.keys


    def getSrc(self):
        return self._src

    def getDest(self):
        return self._dest

    def getWeight(self):
        return self._weight

    def getKey(self):
        return self._key

    def __repr__(self):
        return f"Src = {self._src}, Dest = {self._dest}, Weight = {self._weight}"

