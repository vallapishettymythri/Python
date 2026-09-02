#Count nodes in linked list
def count_nodes(ll):
    count=0
    temp=ll
    while temp!=None:
        count+=1
        temp=temp["link"]
    return count

ll={'data': 10,
 'link': {'data': 20,
  'link': {'data': 30,
   'link': {'data': 40, 'link': {'data': 50, 'link': None}}}}}
count_nodes(ll)
