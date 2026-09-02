#normal form
def normal_form(data):
    result=[]
    for i in data:
        lst=i["subjects"].split(",")
        for value in lst:
            result.append({
                "sid":i["sid"],
                "name":i["name"],
                "subjects":value
            })
    return result
data=[
    {"sid":101,"name":"abc","city":"pune","subjects":"maths,physics,chemistry"},
     {"sid":102,"name":"pqr","city":"hyd","subjects":"hindi,marathi,sanskrit"}
]
normal_form(data)

    