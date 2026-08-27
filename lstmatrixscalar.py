#wAP to find a matrix is scalar matrix
def square(matrix):
    if len(matrix)==len(matrix[0]):
        return True
    else:
        return False
def scalar(matrix):
    if square(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==j:
                    if matrix[i][j]!=matrix[0][0]:
                        return False
                else:
                    if matrix[i][j]!=0:
                        return False
        return True
matrix=[[5,0, 0],[0,5,0],[0,0,5]]
scalar(matrix)