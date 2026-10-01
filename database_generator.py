#Take a database and read..and then transform the name into uppercase.
def read(database):
    for i in database:
        yield i


def transform(database):
    for i in database:
        i["name"]=i["name"].upper()
        yield i
    print(i)
        

database=[
    {"name":"abc","salary":45000},
    {"name":"pqr","salary":50000}
]
call=read(database)
trans=transform(database)
next(call)
next(trans)
next(call)
next(trans)