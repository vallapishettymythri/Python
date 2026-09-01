#Directed graph
graph={}
def create_graph(v1,v2,v3,v4):
    if v1 not in graph:
        graph[v1]=[]
    if v2 not in graph:
        graph[v2]=[]
    if v3 not in graph:
        graph[v3]=[]
    if v4 not in graph:
        graph[v4]=[]
    graph[v1].append(v2)
    graph[v2].append(v3)
    graph[v3].append(v4)
    graph[v4].append(v1)
    return graph
create_graph("A","B","C","D")