#directed graph
class directed_graph_implementation:
    def __init__(self):
        self.graph={}
    def vertex(self,vertex):
        self.graph[vertex]=[]
    def add_edge(self,v1,v2):
        if v1 not in self.graph:
            self.vertex(v1)
        if v2 not in self.graph:
            self.vertex(v2)
        self.graph[v1].append(v2)
        return self.graph
g=directed_graph_implementation()
g.add_edge("A","B")