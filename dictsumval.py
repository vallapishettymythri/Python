#Sum of values of dict
def sum_of_values(dict):
    sum=0
    for key in dict:
        value=key
        sum+=dict[value]
    return sum
dict={
    1:200,
    2:300,
    4:500,
    5:600
}
sum_of_values(dict)