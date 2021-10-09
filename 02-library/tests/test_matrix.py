from cs506 import matrix

#Test empty matrix corner cases
def test_empty():
    mat = []
    try:
        det = matrix.get_determinant(mat)
    except ValueError as e:
        assert str(e) == "Matrix cannot be empty"

    mat = [[[]]]
    try:
        det = matrix.get_determinant(mat)
    except ValueError as e:
        assert str(e) == "Matrix cannot be empty"

#Test 1-D matrices
def test_1D():
    for i in range(-1, 20):
        mat = [i]
        assert matrix.get_determinant(mat) == i

#Test multi-dimensional valid matrices
def test_valid_matrices():

    #2x2 case
    mat_2x2 = [[2, 3], [4,5]]
    assert matrix.get_determinant(mat_2x2) == -2

    #3x3 case
    mat_3x3 = [[7, 5, 8], [78,9, 14], [-3, 89, 12]]
    assert matrix.get_determinant(mat_3x3) == 42896

    #4x4 case
    mat_4x4 = [[7, 12, 8, 47], [69, 18, 22, 109], [89, -989, 12, 14], [1, 0, 7, 890]]
    assert matrix.get_determinant(mat_4x4) == -331522084

    #5x5 case
    mat_5x5 = [[4, 90, 3, 47, 13], 
                [89, 16, 2, 3, 0], 
                [11, -90, 1, 22, -3.4], 
                [4, 8, 89, 8, 7.8],
                [12, 89, 0, 7, 9]]
    det = matrix.get_determinant(mat_5x5)
    assert round(det, 1) == 98192663.6

#Test non-square maatrices
def test_non_square_matrices():

    mat_3x2 = [[1,2], [4, 5], [8,9]]
    try:
        det = matrix.get_determinant(mat_3x2)
    except ValueError as e:
        assert str(e) == "Matrix must be square"

    mat_irregular = [[1,2, 3], [4, 5, 8], [8,9]]
    try:
        det = matrix.get_determinant(mat_irregular)
    except ValueError as e:
        assert str(e) == "Matrix must be square"





