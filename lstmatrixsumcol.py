#sum of each column in matrix
def sumcolum(matrix):
    for j in range(len(matrix)):
        col_sum=0
        for i in range(len(matrix[j])):
            col_sum+=matrix[i][j]
        print(col_sum)
matrix=[[1,2,3],[5,6,7],[7,8,9]]
sumcolum(matrix)