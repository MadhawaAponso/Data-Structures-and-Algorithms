class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def add(self,vertex,edge):
        self.gdict[vertex].append(edge)
        
customDict={"a":["b,c"],
            "b":["a","d","e"],
            "c":["a","e"],
            "d":["b","e","f"],
            "e":["d","f","c"],
            "f":["d","e"]}

Graph1 = Graph(customDict)
# Graph1.add("d",'a')
print(Graph1.gdict)