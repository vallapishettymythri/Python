#WAP to sum of elements in matrix
def sums(matrix):
    summat=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            summat+=matrix[i][j]
    return summat
matrix=[[1,2,3],[4,5,6],[7,8,9]]
sums(matrix)