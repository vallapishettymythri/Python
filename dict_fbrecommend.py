#part of face book recommendation system
def create_graph(graph,p):
    empty_list=[]
    for i in graph[p]:
        for j in graph[i]:
            if j!=p and j not in graph[p]:
                empty_list.append(j)
    return empty_list

graph={
    "p1":["p2","p3"],
    "p2":["p1","p4"],
    "p3":["p1","p4"],
    "p4":["p2","p3"]
       
}
p="p1"
create_graph(graph,p)