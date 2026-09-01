#Undirected graph
graph={}
def create_graph(v1,v2):
    if v1 not in graph:
        graph[v1]=[]
    if v2 not in graph:
        graph[v2]=[]
    graph[v1].append(v2)
    graph[v2].append(v1)
    return graph
create_graph("A","B")