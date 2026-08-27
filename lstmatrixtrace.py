#wap to find the trace of a matrix
#sum of all diagonal elements
def trace(matrix):
    trace=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i==j:
                trace+=matrix[i][j]
    return trace
matrix=[[1,2,3],[4,5,6],[7,8,9]]
trace(matrix)