from mx import *
import evan

for i in range(100):
    a = Matrix(randmat(2))
    while det(a) != 2:
        a = Matrix(randmat(2))
    print("-----------------------\nMatrix A")
    print(a)
    print("4A^-1")
    print(4 * a.inv())
    print(f"|4A^-1| = {det(4 * a.inv())}\n")
    


