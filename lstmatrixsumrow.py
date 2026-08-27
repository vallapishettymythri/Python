#Sum of each row present in the matrix
def sumrow(matrix):
    for i in range (len(matrix)):
        row_sum=0
        for j in range(len(matrix[i])):
            row_sum+=matrix[i][j]
        print(row_sum)
matrix=[[1,2,3],[5,6,7],[7,8,9]]
sumrow(matrix)