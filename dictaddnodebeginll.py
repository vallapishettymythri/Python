#adding node at beginning
def add_node(ll,node):
    new_node={
        "data":node,
        "link":ll
    }
    return new_node
ll={'data': 10,
 'link': {'data': 20,
  'link': {'data': 30,
   'link': {'data': 40, 'link': {'data': 50, 'link': None}}}}}
add_node(ll,1000)