Matrix class

    1)creating

    a = Matrix([[1,0],[2,-3]])
    b = Matrix("i",2) #can also be O 

    2)operations

    a + b
    a - b
    a * b
    c = a.inv() #returns inverse matrix if exists else None
    c = a.copy()
    
Other funcs

    c = adj(matrix) # returns adjoint of matrix
    d = det(matrix) # return determinant
    randmat(size) #genrates random square matrix value C [-3.4]