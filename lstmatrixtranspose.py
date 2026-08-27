#Transpose of matrix
def transpose(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if i<j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    print(matrix)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix)