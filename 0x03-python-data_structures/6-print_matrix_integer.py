#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of ints"""
    a = np.array([[1,2,3],[3,4,5],[7,8,9]])

    s = [[str(e) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
