#WAP to check a matrix is lower triangle
def check_utm(matrix):
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i<j and matrix[i][j]!=0:
                    return False
    return True
                    
matrix=[[2,0,0],[5,7,0],[1,2,9]]
check_utm(matrix)