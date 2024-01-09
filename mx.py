from random import randint


class Matrix:

    def __init__(self, data, size=None):
        if data in ("O", "I", "o", "i"):
            self.m = self.n = size
            self.createMatrix(data.lower())
        else:
            self.m = len(data[0])
            self.n = len(data)
            self.data = data

    def createMatrix(self, types):
        if types == 'o':
            self.data = [[0 for _ in range(self.m)]for __ in range(self.n)]
        else:
            self.data = [[1 if _ == __ else 0 for _ in range(
                self.m)] for __ in range(self.n)]

    def __repr__(self):
        line = [" ".join(map(lambda x: str(round(x, 2)), (row)))
                for row in self.data]

        return "\n".join(line) + "\n"

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            self.new = [[self.data[y][x] * other for x in range(self.m)] for y in range(self.n)]
            return Matrix(self.new)

        if type(other) != Matrix:
            raise type(other) + "cant be mutiplyed with matrix"

        if self.n != other.m:
            raise f"cant multiple ({self.m},{self,n}) and ({other.m,other.n})"

        othert = other.t().data
        self.new = [[0 for x in range(self.m)] for y in range(self.n)]
        for y, myrow in enumerate(self.data):
            for x, otherrow in enumerate(othert):
                self.new[y][x] = sum(map(lambda x, y: x * y, myrow, otherrow))

        return Matrix(self.new)

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            self.new = [
                [self.data[y][x] * other for x in range(self.m)] for y in range(self.n)]
            return Matrix(self.new)

    def __add__(self, other):
        if not type(other) == Matrix:
            return
        if other.m != self.m or other.n != self.n:
            return

        self.new = [[self.data[y][x] * other.data[y][x]
                     for x in range(self.m)] for y in range(self.n)]

        return Matrix(self.new)

    def __eq__(self, other):
        if self.m != other.m or self.n != other.n:
            return False
        for j in range(self.n):
            for i in range(self.m):
                if round(self.data[j][i], 2) != round(other.data[j][i], 2):
                    # print(self.data[j][i] , other.data[j][i],other)
                    return False
        return True

    def __nq__(self, other):
        return not self.__eq__(other)

    def t(self):
        """ returns transpose of matrix """
        if self.n != self.m:
            return
        return Matrix(list(map(list, zip(*self.data))))

    def inv(self):
        """ returns inverse of matrix if exists else show message """
        mdet = det(self)
        if mdet == 0:
            print("No inverse")
            return None
        myadj = adj(self)

        return (1/mdet) * myadj

    def copy(self):
        """ returns copy of matrix """
        return Matrix(self.data)


def adj(matrix):
    """ returns adj matrix """
    if matrix.m != matrix.n:
        raise "Not Square Matrix for adj"
    if matrix.n == 2:
        # 00 01
        # 10 11
        mat = matrix.data

        new = [
            [mat[1][1], -mat[0][1]],
            [-mat[1][0], mat[0][0]]

        ]
        return Matrix(new)
    if matrix.n != 3:
        raise "Matirx size not 2 or 3. Received:" + matrix.n

    # 00 01 02
    # 10 11 12
    # 20 21 22
    mat = matrix.data
    m22 = mat[2][2]
    m11 = mat[1][1]
    m12 = mat[1][2]
    m21 = mat[2][1]
    m10 = mat[1][0]
    m20 = mat[2][0]
    m01 = mat[0][1]
    m02 = mat[0][2]
    m00 = mat[0][0]

    new = [
        [m22 * m11 - m12 * m21, -m10 * m22 + m20 * m12, m10 * m21 - m11 * m20],
        [-m01 * m22 + m21 * m02, m00 * m22 - m02 * m20, -m00 * m21 + m01 * m20],
        [m01 * m12 - m11 * m02, -m00 * m12 + m10 * m02, m00 * m11 - m01 * m10]
    ]

    new = list(map(list, zip(*new)))
    return Matrix(new)


def det(matrix):
    """ give determinant of matrix """
    if matrix.m != matrix.n:
        raise "Not Square Matrix for Determinat"
        return
    mat = matrix.data
    if matrix.m == 2:
        return mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
    if matrix.m == 3:
        m22 = mat[2][2]
        m11 = mat[1][1]
        m12 = mat[1][2]
        m21 = mat[2][1]
        m10 = mat[1][0]
        m20 = mat[2][0]
        return mat[0][0] * (m11 * m22 - m12 * m21) - mat[0][1] * (m10 * m22 - m12 * m20) + mat[0][2] * (m10 * m21 - m11 * m20)


def randmat(size=3):
    """ generates random square matrix of give size """
    return [[randint(-3, 4) for _ in range(size)] for __ in range(size)]

def help():
    print("Matrix class")
    print("""
    data / I / O
    add + 
    multiply *
    inv
    copy
    """)
    print("Other funcs""")
    print("""
    adj(matrix)
    det(matrix)
    randmat(size) #genrates random square matrix value C [-3.4]
    """)

if __name__ == "__main__":

    # know case
    sample = Matrix([[1, 2, 3], [4, 2, 1], [7, 8, 9]])
    assert sample * sample.inv() == Matrix("I", 3), "something is wrong"
    # 2x2 random matrix
    sample = Matrix(randmat(2))
    assert sample * sample.inv() == Matrix("I", 2) or sample.inv() == None, "something is wrong"
    # 3x3 random matrix
    sample = Matrix(randmat(3))
    assert sample * sample.inv() == Matrix("I", 3) or sample.inv() == None, "something is wrong"

    print("ALL TESTS SUCCESS")

    help()
