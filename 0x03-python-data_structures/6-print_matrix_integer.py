#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for rowvrb in range(len(matrix)):
            for itemvrb in range(len(matrix[rowvrb])):
                if itemvrb != len(matrix[rowvrb]) - 1:
                    endspacevrb = ' '
                else:
                    endspacevrb = ''
                print("{:d}".format(matrix[rowvrb][itemvrb]), end=endspacevrb)
            print()
