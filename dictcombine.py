#Combine two dictionaries.Add values if keys are same else add it to the dictionary.
def combine(d1,d2):
    result={}
    for key in d1:
        if key in d2:
            result[key]=d1[key]+d2[key]
        else:
            result[key]=d1[key]
    for key in d2:
        if key not in result:
            result[key]=d2[key]
    return result
        

d1={
    1:200,
    3:500,
    5:600
}
d2={
    3:500,
    5:700,
    8:900
}
combine(d1,d2)