class Graphs:
    def __init__(self):
        self.gdict = {}
    
    def add_vertex(self,vertex):
        if vertex  not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])
        
    def add_edges(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        else:return False
    
    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            if vertex1 in self.gdict[vertex2]:
                self.gdict[vertex2].remove(vertex1)
                self.gdict[vertex1].remove(vertex2)
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.gdict.keys():
            for x in self.gdict[vertex]:
                self.gdict[x].remove(vertex)
            del self.gdict[vertex]
            return True
        return False
    
    # traversing grpah
    def BreathFirstSearch(self,vertex):
        tested = list()
        tested.append(vertex)
        queue = []
        queue.append(vertex)
        while queue:
            data = queue.pop(0)
            for values in self.gdict[data]:
                if values not in tested:
                    tested.append(values)
                    queue.append(values)
        return tested
    #traversing graph
    def DepthFirstSearch(self, vertex):
        visited = []
        stack = [vertex]  # Use a stack for DFS
    
        while stack:
            current = stack.pop()
        
            if current not in visited:
                visited.append(current)
                for neighbor in reversed(self.gdict[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        print(stack)
                    
        return visited
             
        
        
                
##################################################################################################################################

custom_graph = Graphs()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_vertex("E")


custom_graph.add_edges("A","B")
custom_graph.add_edges("A","C")
custom_graph.add_edges("B","E")
custom_graph.add_edges("D","E")
custom_graph.add_edges("D","C")

custom_graph.print_graph()

print("After removing")

# # custom_graph.remove_edge("B","H")
# custom_graph.remove_vertex("F")
custom_graph.print_graph()

print(custom_graph.BreathFirstSearch("A"))
print(custom_graph.DepthFirstSearch("A"))