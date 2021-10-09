
def get_determinant(matrix):
    """
    Computes the determinant of a matrix
    :param matrix - a list of lists of numbers
    :return - the determinant of the matrix
    """

    #Check for empty list
    if not bool(matrix):
        raise ValueError("Matrix cannot be empty")
    
    #allow single item matrices to pass
    elif len(matrix) == 1:
        pass
    
    #Check for non square matrix
    elif (len(matrix) != len(matrix[0])) or any([len(row) != len(matrix[0]) for row in matrix]):
        raise ValueError("Matrix must be square")

    #1x1 case
    if len(matrix) == 1:
        return matrix[0]
    #2x2 case
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    #3x3
    elif len(matrix) == 3:
        return (matrix[0][0] * get_determinant([matrix[1][-2:], matrix[2][-2:]]) 
                - matrix[0][1] * get_determinant([matrix[1][::len(matrix[1])-1],  matrix[2][::len(matrix[2])-1]]) 
                + matrix[0][2] * get_determinant([matrix[1][:2],  matrix[2][:2]]))

    #4x4 and greater - computer recursively
    else:
        det = 0
        for column_idx, element in enumerate(matrix[0]):
            reduced_mat = []
            for row in matrix[1:]:
                reduced_row = [value for index, value in enumerate(row) if index != column_idx]
                reduced_mat.append(reduced_row)
            if column_idx%2:
                 det -= element * get_determinant(reduced_mat)
            else:
                det += element * get_determinant(reduced_mat)
        return det


