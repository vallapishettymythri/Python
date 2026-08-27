#WAP to search an element in matrix
def searching(matrix,element):
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==element:
                return True
    return False
matrix=[[2,3,5],[7,8,9],[4,5,10]]
element=int(input("element:"))
searching(matrix,element)