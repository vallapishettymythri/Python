#WAP to addition of 2 matrix
def add(m1,m2):
    result=[[0,0],[0,0]]
    for i in range (len(m1)):
        for j in range (len(m1[0])):
            result[i][j]=m1[i][j]+m2[i][j]
    return result
m1=[[2,3],[5,6]]
m2=[[1,2],[3,1]]
add(m1,m2)